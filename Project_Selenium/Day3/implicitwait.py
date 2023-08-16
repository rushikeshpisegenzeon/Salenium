from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time

# serv_obj = Service("C:\Selenium Training\Salenium\Drivers\edgedriver_win64\msedgedriver.exe")
serv_obj = Service()
driver = webdriver.Edge(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.google.com")
driver.maximize_window()

searchBox = driver.find_element(By.XPATH,"//textarea[@id='APjFqb']")
searchBox.send_keys("Selenium")
searchBox.submit()

driver.find_element(By.XPATH,"//h3[normalize-space()='Selenium']").click()
# time.sleep(5)

driver.quit()
