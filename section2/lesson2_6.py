from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/execute_script.html')

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    x_value = browser.find_element(By.ID, 'input_value').text
    input_answer = browser.find_element(By.ID, 'answer')
    input_answer.send_keys(str(calc(x_value)))

    robot_checkbox = browser.find_element(By.CSS_SELECTOR, '[for=robotCheckbox]')
    robot_checkbox.click()
    robot_radio = browser.find_element(By.CSS_SELECTOR, '[for=robotsRule]')
    browser.execute_script("return arguments[0].scrollIntoView(true);",robot_radio)
    robot_radio.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, '.btn-primary')
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)
    submit_button.click()


finally:
    time.sleep(10)
    browser.get()