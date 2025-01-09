from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link =  "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("ab")

    button = browser.find_element(By.XPATH, "//button[@type='submit']") # <button type="submit" class="btn">Submit</button>
    button.click()

# //button[@type="form-control"]

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла