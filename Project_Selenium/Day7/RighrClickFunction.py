from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time
#selenium4
serv_obj = Service()
driver = webdriver.Edge(service=serv_obj)

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()
time.sleep(5)

btn = driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")
act = ActionChains(driver)
act.context_click(btn).perform()  #right Click
time.sleep(5)
