from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time

serv_obj = Service("C:\Selenium Training\Salenium\Drivers\edgedriver_win64\msedgedriver.exe")
driver = webdriver.Edge(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
time.sleep(5)

driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
time.sleep(5)

driver.quit()
time.sleep(5)