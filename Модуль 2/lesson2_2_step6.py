from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math

link = "http://suninjuly.github.io/execute_script.html"
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

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    
    ch_b = browser.find_element(By.ID, value2).click()
    r_b = browser.find_element(By.ID, value3).click()
    
    button.click()
    
finally:
    time.sleep(10)
    browser.quit()
    
