from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    X = browser.find_element(By.ID, "input_value")

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(calc(X.text))

    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)


    inputs = [browser.find_element(By.ID, "robotCheckbox"),
              browser.find_element(By.ID, "robotsRule")]

    for line in inputs:
        line.click()

    button.click()


finally:
    time.sleep(10)
    browser.quit()

