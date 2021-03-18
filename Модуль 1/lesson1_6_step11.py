from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

value1 = "first_block .first"
value2 = "first_block .second"
value3 = "first_block .third"

text = "Поле заполнено"
exp_text = "Congratulations! You have successfully registered!"

try:
    browser = webdriver.Chrome()
    browser.get(link2)

    input1 = browser.find_element(By.CLASS_NAME, value1)
    input1.send_keys(text)

    input2 = browser.find_element(By.CLASS_NAME, value2)
    input2.send_keys(text)      

    input3 = browser.find_element(By.CLASS_NAME, value3)
    input3.send_keys(text)
    
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
    
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert exp_text == welcome_text
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
