from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time

serv_obj = Service("C:\Salenium Training\Salenium\Drivers\edgedriver_win64\msedgedriver.exe")
driver = webdriver.Edge(service=serv_obj)
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")

driver.find_element(By.ID,"Email").clear()
driver.find_element(By.ID,"Email").send_keys("admin@yourstore.com")
time.sleep(5)

driver.find_element(By.ID,"Password").clear()
driver.find_element(By.ID,"Password").send_keys("admin")
time.sleep(5)

driver.find_element(By.XPATH,'/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button').click()
time.sleep(5)

act_title = driver.title
exct_title = "Dashboard / nopCommerce administration"

if act_title==exct_title:
    print("Tested Sucessfully!!")
else:
    print("Failed!")



driver.close()