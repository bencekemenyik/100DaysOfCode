GOOGLE_SHEET_PRICES_ENDPOINT = "your-sheety-google-sheet-link"
GOOGLE_SHEET_USERS_ENDPOINT = "your-sheety-google-sheet-link"
import requests

class DataManager:

    def get_sheet_data(self):
        response = requests.get(url=GOOGLE_SHEET_PRICES_ENDPOINT)
        response.raise_for_status()
        result = response.json()["prices"]
        return result

    def update_iata_code(self, row_id, iata_code):
        params ={
            "price": {
                "iataCode": iata_code
            }
        }
        requests.put(url=f"{GOOGLE_SHEET_PRICES_ENDPOINT}/{row_id}", json=params)

    def get_users_data(self):
        response = requests.get(url=GOOGLE_SHEET_USERS_ENDPOINT)
        response.raise_for_status()
        result = response.json()["users"]
        return result