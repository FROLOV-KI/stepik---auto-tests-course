from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math

link1 = "http://suninjuly.github.io/find_link_text"
value1 = "input"
value2 = "last_name"
value3 = "city"
value4 = "country"

try:
    browser = webdriver.Chrome()
    browser.get(link1)
    
    code = str(math.ceil(math.pow(math.pi, math.e)*10000))
    print(code)
    link2 = browser.find_element_by_link_text(code)
    time.sleep(10)
    link2.click()
    
    input1 = browser.find_element(By.TAG_NAME, value1)
    input1.send_keys("Ivan")

    input2 = browser.find_element(By.NAME, value2)
    input2.send_keys("Petrov")

    input3 = browser.find_element_by_class_name(value3)
    input3.send_keys("Smolensk")

    input4 = browser.find_element(By.ID, value4)
    input4.send_keys("Russia")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
    
