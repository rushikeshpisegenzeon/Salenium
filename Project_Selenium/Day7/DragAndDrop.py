from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time
#selenium4
serv_obj = Service()
driver = webdriver.Edge(service=serv_obj)

driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()
time.sleep(5)

rome_ele = driver.find_element(By.XPATH,"//div[@id='box6']")
italy_ele = driver.find_element(By.XPATH,"//div[@id='box106']")

act = ActionChains(driver)
act.drag_and_drop(rome_ele,italy_ele).perform() #drag and drop operation
time.sleep(5)

wsh_ele = driver.find_element(By.XPATH,"//div[@id='box3']")
us_ele = driver.find_element(By.XPATH,"//div[@id='box103']")

act = ActionChains(driver)
act.drag_and_drop(wsh_ele,us_ele).perform() #drag and drop operation
time.sleep(5)

