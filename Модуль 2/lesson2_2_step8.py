from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import os

link = "http://suninjuly.github.io/file_input.html"

value1 = "firstname"
value2 = "lastname"
value3 = "email"

text = "Поле заполнено"

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, "2_2_step8.txt")

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, value1)
    input1.send_keys(text)

    input2 = browser.find_element(By.NAME, value2)
    input2.send_keys(text)      

    input3 = browser.find_element(By.NAME, value3)
    input3.send_keys(text)

    download = browser.find_element(By.ID, "file")
    download.send_keys(file_path)
    
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
