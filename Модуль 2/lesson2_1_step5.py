from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math

link = "http://suninjuly.github.io/math.html"
value = "input_value"
value1 = "answer"
value2 = "robotCheckbox"
value3 = "robotsRule"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_text = browser.find_element(By.ID, value).text
    ans_field = browser.find_element(By.ID, value1)
    
    ans = calc(x_text)

    ans_field.send_keys(ans)

    ch_b = browser.find_element(By.ID, value2).click()
    r_b = browser.find_element(By.ID, value3).click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    
finally:
    time.sleep(10)
    browser.quit()
    
