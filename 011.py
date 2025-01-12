from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "https://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan Ivanov")

    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Petrov")

    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("avadakedavra@yandex.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')

    element = browser.find_element(By.CSS_SELECTOR, "input#file")
    element.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
finally:
    time.sleep(3)
