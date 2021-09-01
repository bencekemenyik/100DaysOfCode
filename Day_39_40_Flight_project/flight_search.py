import requests
from flight_data import FlightData
from pprint import pprint

KIWI_API_KEY = "your-kiwi-api-key"
KIWI_API_SEARCH_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"



class FlightSearch:

    def get_iata_code(self, city_name):
        headers = {
            "apikey": KIWI_API_KEY
        }
        parameters = {
            "term": city_name
        }
        response = requests.get(url="https://tequila-api.kiwi.com/locations/query", params=parameters, headers=headers)
        data = response.json()
        return data["locations"][0]["code"]

    def search_flight(self, fly_to):
        flight_data = FlightData(fly_to)
        headers = {
            "apikey": KIWI_API_KEY
        }
        parameters = {
            "fly_from": flight_data.fly_from,
            "fly_to": flight_data.fly_to,
            "date_from": flight_data.date_from,
            "date_to": flight_data.date_to,
            "flight_type": flight_data.flight_type,
            "nights_in_dst_from": flight_data.nights_in_dst_from,
            "nights_in_dst_to": flight_data.nights_in_dst_to,
            "limit": flight_data.limit,
            "curr": flight_data.curr,
            "max_stopovers": flight_data.max_stopovers,
        }
        response = requests.get(url=KIWI_API_SEARCH_ENDPOINT, params=parameters, headers=headers)
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"no direct flights available to {flight_data.fly_to}")
            print("Trying with 1 stop overs.")
            parameters["max_stopovers"] = 1
            response = requests.get(url=KIWI_API_SEARCH_ENDPOINT, params=parameters, headers=headers)
            try:
                data = response.json()["data"][0]
            except IndexError:
                print(f"No flight to {flight_data.fly_to} was found with 1 stop overs.")
                return None
            else:
                flight_data.price = data['price']
                flight_data.departure_city_name = data["route"][0]["cityFrom"]
                flight_data.departure_airport_iata_code = data["route"][0]["flyFrom"]
                flight_data.arrival_city_name = data["route"][1]["cityTo"]
                flight_data.arrival_airport_iata_code = data["route"][1]["flyTo"]
                flight_data.outbound_date = data['route'][0]['local_departure'].split('T')[0]
                flight_data.inbound_date = data['route'][2]['local_departure'].split('T')[0]
                return flight_data
        else:
            flight_data.price = data['price']
            flight_data.departure_city_name = data['cityFrom']
            flight_data.departure_airport_iata_code = data['flyFrom']
            flight_data.arrival_city_name = data['cityTo']
            flight_data.arrival_airport_iata_code = data['flyTo']
            flight_data.outbound_date = data['route'][0]['local_departure'].split('T')[0]
            flight_data.inbound_date = data['route'][1]['local_departure'].split('T')[0]
            return flight_data

