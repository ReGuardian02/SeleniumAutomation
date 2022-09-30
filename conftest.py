import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])


@pytest.fixture
def browser():
    print("\nStarting browser...")
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    yield browser
    print("\nQuitting browser..")
    browser.quit()