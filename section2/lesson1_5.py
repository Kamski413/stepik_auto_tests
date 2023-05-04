from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("https://suninjuly.github.io/math.html")

try:
    x_value = browser.find_element(By.ID, 'input_value')
    y = calc(x_value.text)
    input_answer = browser.find_element(By.ID, 'answer')
    input_answer.send_keys(str(y))

    robot_checkbox = browser.find_element(By.CSS_SELECTOR, '[for=robotCheckbox]')
    robot_checkbox.click()

    robot_radio = browser.find_element(By.CSS_SELECTOR, '[for=robotsRule]')
    robot_radio.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, '.btn-default')
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()