from flask import Flask, render_template, request, session
import keys
import openai
from googlemaps import places, Client
import pickle
google = keys.google
app = Flask(__name__, static_url_path='/static')
openai.api_key = keys.openaiKey
app.secret_key = 'your_secret_key'  

def getQuery(occassion, interests, budget):
    query = f"{occassion} occassian with interests in {interests} with a ${budget} budget near me"
    return query


@app.route('/')
def main():
    return render_template('index.html',api_key = google)

@app.route('/questions')
def questions():
    return render_template('questions.html')



@app.route('/locations/')
def locations():
    locationList = []

    longitude = request.args.get('longitude')
    latitude = request.args.get('latitude')
    radius = request.args.get('radius')
    occassion = request.args.get('occassian')
    interests = request.args.get('interests')
    budget = request.args.get('budget')
    session['query'] = getQuery(occassion, interests, budget)
    interests = interests.split(", ")
    gmaps = Client(key=google)

    for i in interests:
        places_data = gmaps.places(query=getQuery(occassion, i, budget), location=(latitude, longitude), radius=radius)['results']
        for place in places_data:
            if place.get('business_status') == 'OPERATIONAL':
                operational_place = {
                    'name': place.get('name'),
                    'formatted_address': place.get('formatted_address'),
                    'price_level': place.get('price_level', None),
                    'type': place.get('types', None),
                    'location':place.get('geometry')['location'],
                    'photo':place.get('photos')[0]['photo_reference']
                }
                locationList.append(operational_place)
    markers = ""
    for i in locationList:
        markers+= f"""
                var marker = new google.maps.Marker({{
                    position: {i['location']},
                    map: null,
                    title: "{i['name']}"
                }});
                markers.push(marker);
            """
    save_data_to_file(locationList)
    return render_template('locations.html', locationList = locationList, len=len(locationList), api_key = google, markers=markers)

@app.route('/results/')
def results():
    locationList = load_data_from_file()
    chosen_locations = []
    index_array = request.args.get('indexes')
    if index_array:
        index_array = list(index_array.split(','))
        for i in index_array:
            chosen = {
                "name": locationList[int(i)]['name'],
                "tags": locationList[int(i)]['type'],
                "price": locationList[int(i)]['price_level'],
            }
            chosen_locations.append(chosen)
    response = planDay(session.get('query'), chosen_locations)
    return render_template('results.html', response=response)


def load_data_from_file():
    try:
        with open('location_data.pkl', 'rb') as file:
            location_dict = pickle.load(file)
    except FileNotFoundError:
        # If the file doesn't exist yet, return an empty dictionary
        location_dict = {}
    return location_dict

def save_data_to_file(location_dict):
    with open('location_data.pkl', 'wb') as file:
        pickle.dump(location_dict, file)


def planDay(query, locations):
    prompt = "Plan me a day where I have a "+query+" and these are my list of locations" + str(locations)
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    max_tokens=300,
    messages = [
        {"role": "system", "content" : "You give a plan for a day with an occassian and a list of locations."},
        {"role": "user", "content" :  prompt},
    ]
    )
    return response["choices"][0]["message"]["content"]


app.run()


