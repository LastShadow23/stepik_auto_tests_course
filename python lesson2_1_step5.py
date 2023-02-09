from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    X = browser.find_element(By.ID, "input_value")
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(calc(X.text))

    inputs = [browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']"),
              browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")]

    for line in inputs:
        line.click()

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()


finally:
    time.sleep(10)
    browser.quit()

