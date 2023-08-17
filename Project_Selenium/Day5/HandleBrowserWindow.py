import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service()
driver = webdriver.Edge(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

# windowid = driver.current_window_handle
# print(windowid)  #4C945DB51801C55F65B384F9F479EFBE
time.sleep(5)
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
time.sleep(5)
windowsIds=driver.window_handles


for winId in windowsIds:
    driver.switch_to.window(winId)
    print(driver.title)
    if driver.title=="OrangeHRM":
        driver.close()
