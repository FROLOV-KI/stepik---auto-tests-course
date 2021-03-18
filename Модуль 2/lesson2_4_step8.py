from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "http://suninjuly.github.io/explicit_wait2.html"
value = "input_value"
value1 = "answer"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    

    exp_text = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button = browser.find_element(By.ID, "book").click()

    button = browser.find_element(By.ID, "solve")

    browser.execute_script('return arguments[0].scrollIntoView(true);', button)
    
    x_text = browser.find_element(By.ID, value).text
    print(x_text)
    ans_field = browser.find_element(By.ID, value1)
    
    ans = calc(x_text)

    ans_field.send_keys(ans)

    button.click()
    
finally:
    time.sleep(10)
    browser.quit()
    
