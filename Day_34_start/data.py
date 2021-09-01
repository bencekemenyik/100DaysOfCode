import requests


class QuizData:

    def __init__(self):
        PARAMETERS = {
            "amount": 10,
            "type": "boolean",
        }

        response = requests.get("https://opentdb.com/api.php", params=PARAMETERS)
        response.raise_for_status()
        data = response.json()

        self.question_data = data["results"]

