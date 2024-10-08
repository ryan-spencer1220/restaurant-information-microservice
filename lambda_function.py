import requests
import os


def get_place_id(restaurant):
    url = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json'
    params = {
        'input': restaurant,
        'inputtype': 'textquery',
        'key': os.getenv('GOOGLE_PLACES_API_KEY')
    }

    response = requests.get(url, params=params)
    place_id = response.json()['candidates'][0]['place_id']


def get_place_information(place_id):
    details_url = 'https://maps.googleapis.com/maps/api/place/details/json'
    details_params = {
        'place_id': place_id,
        'key': os.getenv('GOOGLE_PLACES_API_KEY')
    }

    details_response = requests.get(details_url, params=details_params)
    res = details_response.json()
    return res['result']


def format_response(event, context):
    restaurant_name = event['queryStringParameters']['restaurant_name']
    place_id = get_place_id(restaurant_name)
    place = get_place_information(place_id)

    hours = place['opening_hours']
    photos = place.get('photos')

    details = {
        'place_id': place.get('place_id'),
        'name': place.get('name'),
        'rating': place.get('rating'),
        'user_ratings_total': place.get('user_ratings_total'),
        'formatted_address': place.get('formatted_address'),
        'phone_number': place.get('formatted_phone_number'),
        'website': place.get('website'),
        "open_now": hours.get('open_now'),
        "hours": hours.get('weekday_text'),
        "photo": photos[0] if photos else None,
        "reviews": place.get('reviews')
    }

    return details
