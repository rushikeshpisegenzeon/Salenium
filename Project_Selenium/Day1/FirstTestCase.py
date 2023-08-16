#Test Case
#---------------------------------------------------------------
# Open Web Browser
# Open URL https://opensource-demo.orangehrmlive.com/
# Enter username (Admin).
# Enter password (admin123).
# Click on Login.
# Capture title of the home page.(Actual title)
# Verify title of the page: OrangeHRM (Expected)
# close browser

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time
#selenium4
serv_obj = Service("C:\Salenium Training\Salenium\Drivers\edgedriver_win64\msedgedriver.exe")
driver = webdriver.Edge(service=serv_obj)
driver.implicitly_wait(5)
driver.get("https://opensource-demo.orangehrmlive.com/")
# time.sleep(5)

driver_1=driver.find_element(By.NAME,"username")
driver_1.send_keys("Admin")
# time.sleep(5)

driver_2=driver.find_element(By.NAME,"password")
driver_2.send_keys("admin123")
# time.sleep(5)

driver_3=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
driver_3.click()
# time.sleep(5)

act_title = driver.title
exp_title = "OrangeHRM"

if act_title == exp_title:
    print("Login Test Passed")
else:
    print("Failed")
driver.close()
