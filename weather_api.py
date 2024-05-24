import requests
from operator import itemgetter
import plotly.express as px 
import json
# key for api
key = "cbdb12873cdcda047a9611beb86ee9f5"
# url that we are connecting to 
# requesting accesses 

# formats it into json style 
major_cities = [
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix", 
    "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose", 
    "Austin", "Jacksonville", "Fort Worth", "Columbus", "San Francisco", 
    "Charlotte", "Indianapolis", "Seattle", "Denver", "Washington", 
    "Boston", "El Paso", "Nashville", "Detroit", "Oklahoma City", 
    "Portland", "Las Vegas", "Memphis", "Louisville", "Baltimore", 
    "Milwaukee", "Albuquerque", "Tucson", "Fresno", "Mesa", 
    "Sacramento", "Atlanta", "Kansas City", "Colorado Springs", "Omaha", 
    "Raleigh", "Miami", "Long Beach", "Virginia Beach", "Oakland", 
    "Minneapolis", "Tulsa", "Arlington", "Tampa", "New Orleans"
]
names, temps, lats, lons = [], [], [], []
labels={"lat": "Latitude", "lon": "Longitude", "text": "Temperature (K)"}
for city in major_cities:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"
    request = requests.get(url)
    response_dict = request.json()
    names.append(response_dict["name"])
    lats.append(response_dict["coord"]["lat"])
    lons.append(response_dict["coord"]["lon"])
    temps.append(response_dict["main"]["temp_max"])
title = "temperature in major flordia cities"

fig = px.scatter_geo(lat=lats, lon=lons, title=title, labels=labels, hover_name=names, custom_data=temps)
fig.show()