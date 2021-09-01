from selenium import webdriver

chrome_driver_path = "D:\Python100Nap\Chrome_driver\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text.split('$')[1])

# search_bar = driver.find_element_by_name("q")

# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))

# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)


# sajat megoldas
event_dictionary = {}

list_of_events = driver.find_elements_by_xpath("/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul/li")
for idx, event in enumerate(list_of_events):
    time_tag = event.find_element_by_css_selector("time")
    time_of_event = time_tag.get_attribute("datetime").split('T')[0]
    a_tag = event.find_element_by_css_selector("a")
    name_of_event = a_tag.text
    event_dictionary[idx] = {
        "time": time_of_event,
        "name": name_of_event,
    }

print(event_dictionary)

# times_list = driver.find_elements_by_css_selector(".event-widget time")
# events_list = driver.find_elements_by_css_selector(".event-widget li a")
# for idx in range(len(times_list)):
#     event_dictionary[idx] = {
#         "time": times_list[idx].get_attribute("datetime").split('T')[0],
#         "name": events_list[idx].text
#     }
#
# print(event_dictionary)

# driver.close()  # Adott tabot zar be
driver.quit()  # Az egesz bongeszot bezarja, inkabb ez jobb