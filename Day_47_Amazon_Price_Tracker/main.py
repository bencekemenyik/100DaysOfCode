import requests
from bs4 import BeautifulSoup
import smtplib


MY_EMAIL = "your-email"
MY_PASSWORD = "your-password"
AMAZON_URL = input("Copy your item's amazon url (link) here: ")
WATCH_LIMIT = float(input("Below what price do you want to get an alert? $"))
WATCHED_ITEM = AMAZON_URL.split('/')[3].replace("-", " ")


HEADERS = {
    "Request Line": "GET / HTTP/1.1",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Accept-Language": "hu-HU,hu;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate",
    "Cookie": "your-info-from-whatsmyheader",
    "Upgrade-Insecure-Requests": "1",
    "X-Http-Proto": "HTTP/1.1",
    "X-Real-Ip": "your-ip-from-whatsmyheader",

}

response = requests.get(url=AMAZON_URL, headers=HEADERS)
amazon_web_page = response.text

soup = BeautifulSoup(amazon_web_page, "html.parser")

price = float(soup.find(name="span", class_="a-size-medium a-color-price priceBlockBuyingPriceString").getText()[1:])


if price < WATCH_LIMIT:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"Subject:{WATCHED_ITEM} Price Alert!\n\nThe product price is now ${price}, below your target price({WATCH_LIMIT}). Buy now!\n{AMAZON_URL}")

