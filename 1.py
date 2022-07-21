from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import math
import time

s = Service("D:\OneDrive\Рабочий стол\web_drivers\chromedriver.exe")
driver = webdriver.Chrome(service=s)
link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    driver.get(link)
    book_button = driver.find_element(By.ID, "book")
    current_price = WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    book_button.click()
    x = int(driver.find_element(By.ID, "input_value").text)
    print(x)
    answer = str(math.log(abs(12 * math.sin(x))))
    field = driver.find_element(By.ID, "answer")
    field.send_keys(answer)
    submit_button = driver.find_element(By.ID, "solve")
    driver.execute_script("return arguments[0].scrollIntoView(true);", submit_button)
    submit_button.click()

finally:
    time.sleep(100)
    driver.quit()