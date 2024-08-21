import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()

@pytest.mark.parametrize("username,password", [
    ("test", "test"),
    ("user2", "pass2"),
    ("user3", "pass3"),
])

def login_test(driver, username, password):
    driver.get("https://trytestingthis.netlify.app/")
    username_field = driver.find_element(By.ID,"uname")
    password_field = driver.find_element(By.ID,"pwd")
    submit_button = driver.find_element(By.XPATH, "//input[@value='Login']")

    username_field.send_keys('username')
    password_field.send_keys('password')
    time.sleep(2)
    submit_button.click()
    assert "Successful" in driver.page_source
    time.sleep(2)