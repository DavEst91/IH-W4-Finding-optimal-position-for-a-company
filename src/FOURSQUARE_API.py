import os
from dotenv import load_dotenv
load_dotenv()
import json, requests


FOURSQUARE_CLIENTID= os.getenv("FOURSQUARE_CLIENTID")
FOURSQUARE_CLIENTSECRET= os.getenv("FOURSQUARE_CLIENTSECRET")

def foursquare(latitude,longitude,tag):
    url = 'https://api.foursquare.com/v2/venues/explore'
    params = dict(
    client_id=FOURSQUARE_CLIENTID,
    client_secret=FOURSQUARE_CLIENTSECRET,
    v='20200401',
    ll=f"{latitude},{longitude}",
    query=tag,
    limit=1)
    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)
    address=" ".join(data["response"]["groups"][0]['items'][0]['venue']["location"]['formattedAddress'])
    distance=data["response"]["groups"][0]['items'][0]['venue']["location"]['distance']
    location=data["response"]["groups"][0]['items'][0]['venue']["location"]
    latitude=data["response"]["groups"][0]['items'][0]['venue']["location"]['lat']
    longitude=data["response"]["groups"][0]['items'][0]['venue']["location"]['lng']
    return address,distance,[latitude,longitude]
