from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time
import os



serv_obj = Service()
driver = webdriver.Edge(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
time.sleep(5)

#driver.save_screenshot(os.getcwd()+"\\homepage.png")
driver.get_screenshot_as_file(os.getcwd()+"\\homepage.png")
# driver.get_screenshot_as_png()
# driver.get_screenshot_as_base64() #save in binary format
driver.quit()