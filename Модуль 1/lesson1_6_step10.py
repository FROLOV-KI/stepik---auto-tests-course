from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/registration1.html"
value = "//input[@required]"
text = "Поле заполнено"
exp_text = "Congratulations! You have successfully registered!"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    elements = browser.find_elements(By.XPATH, value)
    print(len(elements))
    for element in elements:
        element.send_keys(text)

    time.sleep(1)
    
    button = browser.find_element(By.XPATH, "//button[text()=\"Submit\"]")
    button.click()

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert exp_text == welcome_text
finally:
    time.sleep(10)
    browser.quit()
    
