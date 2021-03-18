from selenium import webdriver
import time
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/huge_form.html"
value = "Мой ответ"
value1 = "input"

try:
    browser = webdriver.Chrome()
    browser.get(link)
     
    elements = browser.find_elements(By.TAG_NAME, value1)
    for element in elements:
        element.send_keys(value)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
    
