from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time

# serv_obj = Service("C:\Selenium Training\Salenium\Drivers\edgedriver_win64\msedgedriver.exe")
serv_obj = Service()
driver = webdriver.Edge(service=serv_obj)



driver.get("https://www.snapdeal.com")
driver.get("https://www.amazon.com")

driver.back()
driver.forward()

driver.refresh()

driver.quit()