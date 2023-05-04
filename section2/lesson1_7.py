from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/get_attribute.html')

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    treasure = browser.find_element(By.ID, 'treasure')
    x_value = treasure.get_attribute('valuex')

    input_answer = browser.find_element(By.ID, 'answer')
    input_answer.send_keys(str(calc(x_value)))

    robot_checkbox = browser.find_element(By.ID, 'robotCheckbox')
    robot_checkbox.click()

    robot_radio = browser.find_element(By.ID, 'robotsRule')
    robot_radio.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, '.btn-default')
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()