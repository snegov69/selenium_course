from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
       return str(math.log(abs(12*math.sin(int(x)))))

    x_element = browser.find_element(By.CSS_SELECTOR, "span#input_value.nowrap")
    x = x_element.text
    y = calc(x)

    button = browser.find_element(By.ID, "robotCheckbox")
    button.click()

    button = browser.find_element(By.ID, "robotsRule")
    button.click()

    input = browser.find_element(By.TAG_NAME, "input")
    input.send_keys(y)

    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    time.sleep(3)
