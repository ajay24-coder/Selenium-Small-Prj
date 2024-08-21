from datetime import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicity_wait(10)
    #Yield the webdriver instance
    yield driver
    #Close the WebDriver instance
    driver.quit()


def test_google_search(driver):

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://google.com")
    googleSearchBox = driver.find_element(By.ID,"input")
    googleSearchBox.send_keys("Automation")
    googleSearchBox.send_keys(keys.RETURN)
    time.sleep(2)
    print("Test Completed")