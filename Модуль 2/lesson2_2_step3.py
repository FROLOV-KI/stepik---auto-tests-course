from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
value = "num1"
value1 = "num2"
value2 = "dropdown"


def calc(x, y):
    return str(int(x) + int(y))


try:
    br = webdriver.Chrome()
    br.get(link)

    num1 = br.find_element(By.ID, value).text
    num2 = br.find_element(By.ID, value1).text

    res = calc(num1, num2)

    sel = Select(br.find_element(By.ID, value2))
    sel.select_by_visible_text(res)
                               
    button = br.find_element(By.CSS_SELECTOR, "button.btn").click()
    
finally:
    time.sleep(10)
    br.quit()
    
