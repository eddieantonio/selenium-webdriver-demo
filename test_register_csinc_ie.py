import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://register.csinc.ie/")

assert "Log in to CSLinc" in driver.title

# Email element
email_element = driver.find_element(By.ID, "Email")
email_element.send_keys("nobody@example.com")
assert "nobody@example.com" == email_element.get_attribute("value")

driver.close()
