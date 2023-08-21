from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time


serv_obj = Service()
driver = webdriver.Edge(service=serv_obj)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
time.sleep(5)


driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()

countrieslist = driver.find_elements(By.XPATH,"//ul[@id='select2-billing_country-results']/li")

print(len(countrieslist))

for country in countrieslist:
    if country.text=="Brazil":
        country.click()
        break
