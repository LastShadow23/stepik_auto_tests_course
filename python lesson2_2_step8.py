from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    inputs = [browser.find_element(By.NAME, "firstname"),
              browser.find_element(By.NAME, "lastname"),
              browser.find_element(By.NAME, "email")]

    for line in inputs:
        line.send_keys('Check')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, '131.txt')
    element = browser.find_element(By.ID, "file")
    element.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    time.sleep(10)
    browser.quit()

