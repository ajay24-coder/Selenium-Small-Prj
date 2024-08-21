import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from POMDemo.tests.pages.login_page import LoginPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()



def test_login(driver):
    login_page = LoginPage(driver)
    login_page.open_page("https://trytestingthis.netlify.app/")
    time.sleep(1)
    login_page.enter_username("test")
    time.sleep(1)
    login_page.enter_password("test")
    time.sleep(1)
    login_page.click_Login()
    time.sleep(1)

    # driver.get("https://trytestingthis.netlify.app/")
    # username_field = driver.find_element(By.ID,"uname")
    # password_field = driver.find_element(By.ID,"pwd")
    # submit_button = driver.find_element(By.XPATH, "//input[@value='Login']")
    #
    # username_field.send_keys('username')
    # password_field.send_keys('password')
    # time.sleep(2)
    # submit_button.click()
    assert "Successful" in driver.page_source
    time.sleep(2)