import time
from selenium import webdriver
driver = webdriver.Chrome()
time.sleep(7)
driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(7)
textarea = driver.find_element_by_css_selector(".textarea")
textarea.send_keys("get()")
submit_button = driver.find_element_by_css_selector(".submit-submission")
time.sleep(7)
submit_button.click()
time.sleep(7)
driver.quit()
