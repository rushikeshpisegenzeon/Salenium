from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time
#selenium4
serv_obj = Service()
driver = webdriver.Edge(service=serv_obj)

driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
driver.maximize_window()
time.sleep(5)

driver.switch_to.frame("iframeResult") #switch to frame

field1 = driver.find_element(By.XPATH,"//input[@id='field1']")
field1.clear()
field1.send_keys("Rushikesh Pise")

button = driver.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")

act = ActionChains(driver)

act.double_click(button).perform() #double click action will happen
time.sleep(5)