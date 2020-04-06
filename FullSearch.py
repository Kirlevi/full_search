import sys
from io import BytesIO

import requests
from PIL import Image

import GeocoderParams

# program1.py Москва, ул. Ак. Королева, 12

toponym_to_find = " ".join(sys.argv[1:])

toponym = GeocoderParams.address_to_geocode(toponym_to_find)



geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": toponym_to_find,
    "format": "json"}

response = requests.get(geocoder_api_server, params=geocoder_params)

# Долгота и широта:
toponym_longitude, toponym_lattitude = GeocoderParams.get_coordinates(toponym_to_find)


map_params = {
    "ll": ",".join([str(toponym_longitude), str(toponym_lattitude)]),
    "spn": ",".join(GeocoderParams.get_scale(toponym_to_find)),
    "pt": ",".join([str(toponym_longitude), str(toponym_lattitude), 'org']),
    "l": "map"
}

map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)

Image.open(BytesIO(
    response.content)).show()