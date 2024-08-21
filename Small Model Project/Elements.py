import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://google.com")
googleSearchBox = driver.find_element(By.ID,"input")
googleSearchBox.send_keys("Automation")
googleSearchBox.send_keys(keys.RETURN)
#driver.find_element(By.TYPE,"search").click()
time.sleep(5)

driver.get("https://trytestingthis.netlify.app/")
driver.find_element(By.ID,"fname").send_keys("Ajju")
driver.find_element(By.ID,"lname").send_keys("Annu")
time.sleep(5)
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
time.sleep(5)