from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/selects1.html')

try:
    num1 = browser.find_element(By.ID, 'num1').text
    num2 = browser.find_element(By.ID, 'num2').text
    answer = (int(num2)+int(num1))
    select_answer = Select(browser.find_element(By.ID, 'dropdown'))
    select_answer.select_by_value(f'{answer}')
    submit_button = browser.find_element(By.CSS_SELECTOR, '.btn-default')
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()
