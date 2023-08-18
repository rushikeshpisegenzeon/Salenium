from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support import ui
from selenium.webdriver.support.select import Select

#selenium4
serv_obj = Service()
driver = webdriver.Edge(service=serv_obj)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
time.sleep(5)

driver.find_element(By.XPATH,"//input[@id='dob']").click()
time.sleep(5)

datepicker_month = Select(driver.find_element(By.XPATH,"//select[@aria-label='Select month']"))

datepicker_month.select_by_visible_text("Aug")
time.sleep(5)

datepicker_year = Select(driver.find_element(By.XPATH,"//select[@aria-label='Select year']"))

datepicker_year.select_by_visible_text("1998")
time.sleep(5)

dates = driver.find_elements(By.XPATH,"//div[@id='ui-datepicker-div']//table/tbody/tr/td/a")

for date in dates:
    if date.text=="25":
        date.click()
        time.sleep(5)
        break

time.sleep(5)