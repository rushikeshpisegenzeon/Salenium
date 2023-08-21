from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time


serv_obj = Service()
driver = webdriver.Edge(service=serv_obj)

driver.get("https://www.foundit.in/")
driver.maximize_window()
time.sleep(5)

driver.find_element(By.XPATH,"//div[@class='heroSection-buttonContainer_secondaryBtn secondaryBtn']").click()
driver.find_element(By.XPATH,"//input[@id='file-upload']").send_keys("C:\My Documents\CDAC certificate.pdf")
time.sleep(5)