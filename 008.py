from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    el = browser.find_element(By.TAG_NAME, "img")
    x_element = el.get_attribute("valuex")

    y = calc(str(x_element))

    input = browser.find_element(By.TAG_NAME, "input")
    input.send_keys(y)

    button = browser.find_element(By.ID, "robotCheckbox")
    button.click()

    button = browser.find_element(By.ID, "robotsRule")
    button.click()

    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    time.sleep(3)
