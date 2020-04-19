import requests
from amadeus import Client
import os
from dotenv import load_dotenv
load_dotenv()

AMADEUS_APIKEY = os.getenv("AMADEUS_APIKEY")
AMADEUS_APISECRET = os.getenv("AMADEUS_APISECRET")

amadeus =Client(
    client_id=AMADEUS_APIKEY,
    client_secret=AMADEUS_APISECRET
)


def closest_airport(latitude, longitude):
    airport_list=amadeus.reference_data.locations.airports.get(longitude=longitude,latitude=latitude)
    return airport_list.data[0]['name'],airport_list.data[0]['distance']['value']

