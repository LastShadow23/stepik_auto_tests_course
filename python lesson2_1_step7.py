from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "treasure")
    X = x_element.get_attribute("valuex")
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(calc(X))

    inputs = [browser.find_element(By.ID, "robotCheckbox"),
              browser.find_element(By.ID, "robotsRule")]

    for line in inputs:
        line.click()

    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()


finally:
    time.sleep(10)
    browser.quit()

