from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager
from pprint import pprint
import requests
from datetime import datetime, timedelta

KIWI_API_KEY = "your-kiwi-api-key"
GOOGLE_SHEET_ENDPOINT = "your-sheety-google-sheet-link"

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_sheet_data()
user_sheet_data = data_manager.get_users_data()

is_iata_code_column_empty = False
for one_row in sheet_data:
    if len(one_row["iataCode"]) < 1:
        is_iata_code_column_empty = True

print(is_iata_code_column_empty)

if is_iata_code_column_empty:
    for one_row in sheet_data:
        one_row["iataCode"] = flight_search.get_iata_code(one_row["city"])
        data_manager.update_iata_code(one_row["id"], one_row["iataCode"])

for one_row in sheet_data:
    flight_data = flight_search.search_flight(one_row["iataCode"])
    if flight_data is None:
        continue
    if flight_data.price < one_row['lowestPrice']:
        for one_user_row in user_sheet_data:
            notification_manager.send_email(one_user_row["email"], flight_data.get_datas(), flight_data.get_google_link())