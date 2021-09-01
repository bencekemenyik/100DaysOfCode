import requests
from twilio.rest import Client
from html.parser import HTMLParser

class HTMLFilter(HTMLParser):
    text = ""

    def handle_data(self, data):
        self.text += data


STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "your-api-key"
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
PERCENTAGE_THRESHOLD = 5

SMS_SID = "your-account-sid"
SMS_ATK = "your-account-auth-key"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "your-api-key"

# ------------------------------------------------------------------------ STOCK ------------------------------------------------------------------------------------------------ #

parameters_stock = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

response_stock = requests.get(STOCK_ENDPOINT, params=parameters_stock)
print(response_stock.status_code)
response_stock.raise_for_status()
data_stock = response_stock.json()
print(data_stock)

daily_data = data_stock["Time Series (Daily)"]
yesterday_and_before_close_prices = [daily_data[day]["4. close"] for (day, data_stock) in daily_data.items()][:2]
yesterday_closing = round(float(yesterday_and_before_close_prices[0]), 2)
before_yesterday_closing = round(float(yesterday_and_before_close_prices[1]), 2)
if yesterday_closing > before_yesterday_closing:
    symbol = "🔺"
else:
    symbol = "🔻"
print(f"yesterday: {yesterday_closing}, the day before: {before_yesterday_closing}")

difference = round(abs(yesterday_closing - before_yesterday_closing), 2)
print(f"difference: {difference}")

percentage_difference = round((difference / yesterday_closing) * 100, 2)
print(f"difference(%): {percentage_difference}")

# ------------------------------------------------------------------------------ NEWS --------------------------------------------------------------------------------------------#

if percentage_difference > PERCENTAGE_THRESHOLD:

    parameters_news = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
        "sortBy": "relevancy",
    }

    response_news = requests.get(NEWS_ENDPOINT, params=parameters_news)
    print(response_news.status_code)
    response_news.raise_for_status()
    data_news = response_news.json()
    first_three_news = data_news["articles"][:3]
    print(first_three_news)

    important_info = [(news["title"], news["description"]) for news in first_three_news]

    account_sid = SMS_SID
    auth_token = SMS_ATK
    client = Client(account_sid, auth_token)

    f = HTMLFilter()
    for one_news in important_info:
        print(f"Headline: {one_news[0]}")
        f.feed(one_news[1])
        brief = f.text
        f.text = ""
        print(f"Brief: {brief}")

        message = client.messages \
                        .create(
                             body=f"{STOCK_NAME}: {symbol}{percentage_difference}%\nHeadline: {one_news[0]}\nBrief: {brief}",
                             from_='your-trial-number',
                             to='your-phone-number'
                         )

        print(message.status)
