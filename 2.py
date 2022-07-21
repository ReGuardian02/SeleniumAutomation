from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/wait1.html"
s = Service("D:\OneDrive\Рабочий стол\web_drivers\chromedriver.exe")
browser = webdriver.Chrome(service=s)
browser.implicitly_wait(5)

browser.get(link)

button = browser.find_element(By.ID, "verify")
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text