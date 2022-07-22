from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"
s = Service("D:\OneDrive\Рабочий стол\web_drivers\chromedriver.exe")
driver = webdriver.Chrome(service=s)

try:
    driver.get(link)
    currentDir = os.path.abspath(os.path.dirname(__file__))
    fileDir = os.path.join(currentDir, "Pythonus.txt") #файлы находятся в одной папке
    name_field = driver.find_element(By.NAME, "firstname")
    name_field.send_keys("Danya")
    surname_field = driver.find_element(By.NAME, "lastname")
    surname_field.send_keys("Sukhoparov")
    email_field = driver.find_element(By.NAME, "email")
    email_field.send_keys("danilasuhoparov@yandex.ru")
    file_input = driver.find_element(By.CSS_SELECTOR, '[accept=".txt"]')
    file_input.send_keys(fileDir)
    submit_button = driver.find_element(By.CLASS_NAME, "btn")
    submit_button.click()

finally:
    time.sleep(10)
    driver.quit()