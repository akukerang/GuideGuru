from googlemaps import places, Client
import config
gmaps = Client(key=config.API_KEY)

print(gmaps.places(query='romantic', location=(25.761681, -80.191788), radius=40))