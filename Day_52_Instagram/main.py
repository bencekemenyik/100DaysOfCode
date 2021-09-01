from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

chrome_driver_path = "D:/Python100Nap/Chrome_driver/chromedriver.exe"

driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://www.instagram.com/")

try:
    accept_cookies = driver.find_element_by_class_name("aOOlW  bIiDR  ")
except NoSuchElementException:
    pass
else:
    accept_cookies.click()
time.sleep(2)
uname = driver.find_element_by_name("username")
uname.send_keys("your-username")
pw = driver.find_element_by_name("password")
pw.send_keys("your-password")
pw.send_keys(Keys.ENTER)
time.sleep(5)
try:
    accept_shit = driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[1]")
except NoSuchElementException:
    pass
else:
    accept_shit.click()
search_bar = driver.find_element_by_css_selector("._0aCwM input")
search_bar.send_keys("chefsteps")
time.sleep(3)
search_bar.send_keys(Keys.ENTER)
search_bar.send_keys(Keys.ENTER)
time.sleep(3)
followers_button = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
followers_button.click()
time.sleep(10)
follow_buttons = driver.find_elements_by_css_selector(".sqdOP")
for follow_button in follow_buttons:
    follow_button.click()
    time.sleep(1)