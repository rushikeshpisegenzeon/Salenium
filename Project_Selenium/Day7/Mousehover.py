#not work for this website we can choose another website for see the results
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time
#selenium4
serv_obj = Service()
driver = webdriver.Edge(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
time.sleep(5)

#Login
driver.find_element(By.NAME,"username").send_keys("Admin")
time.sleep(5)
driver.find_element(By.NAME,"password").send_keys("admin123")
time.sleep(5)
driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
time.sleep(5)


#Admin-->user management-->users
admin = driver.find_element(By.XPATH,"//li[1]//a[1]//span[1]")
time.sleep(5)
usermgmt = driver.find_element(By.XPATH,"//span[normalize-space()='User Management']")
time.sleep(5)
users = driver.find_element(By.XPATH,"//a[normalize-space()='Users']")
time.sleep(5)

#mousehover action

act = ActionChains(driver)
act.move_to_element(admin).move_to_element(usermgmt).move_to_element(users).click().perform()
time.sleep(5)