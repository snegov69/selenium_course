from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

link = "https://suninjuly.github.io/selects1.html"
def calc(a,b):
    return int(a) + int(b)
try:
    browser = webdriver.Chrome()
    browser.get(link)

    a = browser.find_element(By.ID, "num1").text
    b = browser.find_element(By.ID, "num2").text

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    res = str(calc(a, b))
    select.select_by_value(res)

    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

finally:
    time.sleep(3)
