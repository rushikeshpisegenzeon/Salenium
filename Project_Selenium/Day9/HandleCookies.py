from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time
import os



serv_obj = Service()
driver = webdriver.Edge(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
time.sleep(5)

#Capture Cookies from the browser
cookies = driver.get_cookies()
print("Size of cookies:",len(cookies)) #5

#Print details of all cookies
# for c in cookies:
#     print(c.get('name'),":",c.get('value'))


#Add new cookie to the browser
driver.add_cookie({"name":"MyCookie","value":"123456"})
cookies = driver.get_cookies()
print("Size of cookies after add new cookie:",len(cookies))

#Delete a specific cookie from the browser
driver.delete_cookie("MyCookie")
cookies=driver.get_cookies()
print("Size of cookies after deleted one:",len(cookies))

#Delete all cookies
driver.delete_all_cookies()
cookies=driver.get_cookies()
print("Size of cookies after deleted all:",len(cookies)) #0


driver.quit()