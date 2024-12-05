import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://register.csinc.ie/")

print(driver.title)
time.sleep(18)
driver.close()
