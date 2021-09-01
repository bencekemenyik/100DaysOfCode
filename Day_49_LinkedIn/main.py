from selenium import webdriver
import time

chrome_driver_path = "D:/Python100Nap/Chrome_driver/chromedriver.exe"

driver = webdriver.Chrome(chrome_driver_path)

driver.get(url="https://www.linkedin.com/jobs/search/?f_AL=true&f_E=2&f_WRA=true&geoId=100288700&keywords=python%20developer&location=Hungary")
sign_in = driver.find_element_by_link_text("Sign in")
sign_in.click()
time.sleep(3)
uname = driver.find_element_by_id("username")
uname.send_keys("your-email")
pw = driver.find_element_by_id("password")
pw.send_keys("your-password")
login_page_sign_in = driver.find_element_by_css_selector(".login__form_action_container button")
login_page_sign_in.click()
time.sleep(5)
first_result = driver.find_element_by_class_name("job-card-container")
first_result.click()
time.sleep(3)
save_button = driver.find_element_by_class_name("jobs-save-button")
save_button.click()
time.sleep(3)
follow_button = driver.find_element_by_class_name("follow")
follow_button.click()
# driver.quit()

