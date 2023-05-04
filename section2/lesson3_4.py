from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/alert_accept.html')

try:
    button = browser.find_element(By.CSS_SELECTOR, '.btn-primary')
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()


    x_value = browser.find_element(By.ID, 'input_value').text
    input_answer = browser.find_element(By.ID, 'answer')
    input_answer.send_keys(str(calc(x_value)))

    submit_button = browser.find_element(By.CSS_SELECTOR, '.btn-primary')
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()