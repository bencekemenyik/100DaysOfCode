from selenium import webdriver
import datetime
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "D:\Python100Nap\Chrome_driver\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

# wiki_numer = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[5]/div[1]/div[1]/div/div[3]/a[1]")
# print(wiki_numer.text)

# tech_link = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[5]/div[1]/div[1]/ul/li[8]/a")
# tech_link.click()
# time.sleep(2)
# math_link = driver.find_element_by_xpath('//*[@id="portals-browsebar"]/dl/dd[6]/a')
# math_link.click()

# search_bar = driver.find_element_by_xpath('//*[@id="searchInput"]')
# time.sleep(2)
# search_bar.click()
# time.sleep(2)
# search_bar.send_keys("America")
# time.sleep(2)
# search_button = driver.find_element_by_xpath('//*[@id="searchButton"]')
# time.sleep(2)
# search_button.click()
# time.sleep(2)

# search_bar = driver.find_element_by_name("search")
# search_bar.send_keys("Japan")
# search_bar.send_keys(Keys.ENTER)
# first_result = driver.find_element_by_css_selector(".mw-search-results a")
# first_result.click()

# now = datetime.datetime.now()
#
#
# first_name = driver.find_element_by_name("fName")
# first_name.send_keys("Jozsika")
# last_name = driver.find_element_by_name("lName")
# last_name.send_keys("Zsiros")
# email = driver.find_element_by_name("email")
# email.send_keys("zsiros.jozsika@gmail.com")
# submit = driver.find_element_by_tag_name("button")
# submit.click()
#
# after_now = datetime.datetime.now()
#
# print(after_now-now)

cookie = driver.find_element_by_id("cookie")
time_check = time.time() + 5
time_out = time.time() + 60*5
while True:
    if time.time() > time_out:
        break
    cookie.click()
    if time.time() > time_check:
        money = driver.find_element_by_id("money")
        list_of_items = driver.find_elements_by_css_selector("#store div")
        affordable_items = [item for item in list_of_items if item.get_attribute("class") == ""]
        affordable_items[-1].click()
        # cost_of_items = [int(item.text.split('\n')[0].split('-')[1].strip().replace(",", "")) for item in affordable_items if item.text != ""]
        # max_idx = maxcost_of_items
        time_check = time.time() + 5

# driver.quit()
