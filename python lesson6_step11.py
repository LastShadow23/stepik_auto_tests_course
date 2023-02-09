from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    inputs = [browser.find_element_by_xpath('//input[contains(@class, "first") and @required]'),
              browser.find_element_by_xpath('//input[contains(@class, "second") and @required]'),
              browser.find_element_by_xpath('//input[contains(@class, "third") and @required]')]

    for line in inputs:
        line.send_keys('Check')

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text = browser.find_element_by_tag_name("h1").text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()

