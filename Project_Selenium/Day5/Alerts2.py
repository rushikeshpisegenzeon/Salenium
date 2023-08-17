import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service()
driver = webdriver.Edge(service=serv_obj)

driver.get("https://mypage.rediff.com/login/dologin")
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@value='Login']").click()
time.sleep(5)
driver.switch_to.alert.accept()
