from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/file_input.html')

try:
    first_name = browser.find_element(By.NAME, 'firstname')
    last_name = browser.find_element(By.NAME, 'lastname')
    email = browser.find_element(By.NAME, 'email')
    first_name.send_keys('Name')
    last_name.send_keys('Last name')
    email.send_keys('email')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    file = browser.find_element(By.ID, 'file')
    file.send_keys(file_path)

    submit_button = browser.find_element(By.CLASS_NAME, 'btn')
    submit_button.click()
finally:
    time.sleep(10)
    browser.quit()