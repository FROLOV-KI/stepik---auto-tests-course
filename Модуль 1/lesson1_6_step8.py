from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_xpath_form"
value1 = "input"
value2 = "last_name"
value3 = "city"
value4 = "country"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, value1)
    input1.send_keys("Ivan")

    input2 = browser.find_element(By.NAME, value2)
    input2.send_keys("Petrov")

    input3 = browser.find_element_by_class_name(value3)
    input3.send_keys("Smolensk")

    input4 = browser.find_element(By.ID, value4)
    input4.send_keys("Russia")

    button = browser.find_element(By.XPATH, "//button[text()=\"Submit\"]")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
    
