import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service()
driver = webdriver.Edge(service=serv_obj)
time.sleep(5)
#inject username and password and by pass it
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

driver.find_element(By.XPATH,"//a[normalize-space()='Iframe with in an Iframe']").click()

outerFrame = driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outerFrame)

innerFrame = driver.find_element(By.XPATH,"/html[1]/body[1]/section[1]/div[1]/div[1]/iframe[1]")
driver.switch_to.frame(innerFrame)

driver.find_element(By.XPATH,"//input[@type='text']").send_keys("Rushikesh")
time.sleep(5)

driver.switch_to.parent_frame() #directly switch to parent frame(outerFrame)

