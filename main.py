from flask import Flask, render_template, request
import config
import openai
from googlemaps import places, Client
api_key = config.API_KEY
app = Flask(__name__, static_url_path='/static')
openai.api_key = config.gptapi_key

def getQuery(occassion, interests, budget):
    query = f"{occassion} occassian with interests in {interests} with a ${budget} budget near me"
    return query


@app.route('/')
def main():
    return render_template('index.html',api_key = api_key)

@app.route('/questions')
def questions():
    return render_template('questions.html')



@app.route('/locations/')
def locations():
    locationList = []

    longitude = request.args.get('longitude')
    latitude = request.args.get('latitude')
    radius = request.args.get('radius')
    occassion = request.args.get('occassion')
    interests = request.args.get('interests')
    budget = request.args.get('budget')

    interests = interests.split(", ")
    gmaps = Client(key=config.API_KEY)

    for i in interests:
        places_data = gmaps.places(query=getQuery(occassion, i, budget), location=(latitude, longitude), radius=radius)['results']
        for place in places_data:
            if place.get('business_status') == 'OPERATIONAL':
                operational_place = {
                    'name': place.get('name'),
                    'formatted_address': place.get('formatted_address'),
                    'price_level': place.get('price_level', None),
                    'type': place.get('types', None)
                }
                locationList.append(operational_place)
    return render_template('locations.html', locationList = locationList, len=len(locationList))

@app.route('/results')
def results():
    return render_template('results.html')
    

app.run()


