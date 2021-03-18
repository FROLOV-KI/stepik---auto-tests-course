from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math

link = "http://suninjuly.github.io/redirect_accept.html"
value = "input_value"
value1 = "answer"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    new_window = browser.window_handles[1]

    browser.switch_to.window(new_window)
        
    x_text = browser.find_element(By.ID, value).text
    ans_field = browser.find_element(By.ID, value1)
    
    ans = calc(x_text)

    ans_field.send_keys(ans)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    
finally:
    time.sleep(10)
    browser.quit()
    
