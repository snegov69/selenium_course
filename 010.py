from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://SunInJuly.github.io/execute_script.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "span#input_value.nowrap")
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.TAG_NAME, "input")
    input.send_keys(y)

    button = browser.find_element(By.ID, "robotCheckbox")
    button.click()

    browser.execute_script("window.scrollBy(0, 700);")

    button = browser.find_element(By.ID, "robotsRule")
    button.click()

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(3)