from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time

chrome_driver_path = "D:/Python100Nap/Chrome_driver/chromedriver.exe"

driver = webdriver.Chrome(chrome_driver_path)

GOOGLE_FORM_URL = "your-google-form"
ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

headers = {
    "ACCEPT-LANGUAGE": "hu-HU,hu;q=0.8,en-US;q=0.5,en;q=0.3",
    "USER-AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",

}


response = requests.get(ZILLOW_URL, headers=headers)
response.raise_for_status()
zillow_web_page = response.text

soup = BeautifulSoup(zillow_web_page, "html.parser")
print(soup.prettify())

addresses_fixed = []
links = [link.get("href") for link in soup.select(".list-card-info a")]
links = [link.replace("/b", "https://www.zillow.com/b") for link in links]
prices = [price.text[:6] for price in soup.select(".list-card-info .list-card-price")]
addresses = [address.text for address in soup.select(".list-card-info .list-card-addr")]
for address in addresses:
    if '|' in address:
        address = address.split('|')[1].strip()
    address = address.split("CA")[0] + "CA"
    addresses_fixed.append(address)
for idx in range(len(links)):
    driver.get(url=GOOGLE_FORM_URL)
    time.sleep(3)
    form_address = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    form_address.send_keys(f"{addresses_fixed[idx]}")
    form_price = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    form_price.send_keys(f"{prices[idx]}")
    form_link = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    form_link.send_keys(f"{links[idx]}")
    form_send = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')
    form_send.click()




