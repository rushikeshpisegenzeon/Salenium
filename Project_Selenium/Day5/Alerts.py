import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service()
driver = webdriver.Edge(service=serv_obj)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

#opens alert window
driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
time.sleep(5)

alertwindow = driver.switch_to.alert

print(alertwindow.text)
alertwindow.send_keys("Welcome Rushikesh Pise")
alertwindow.accept()
#alertwindow.dismiss()
time.sleep(5)