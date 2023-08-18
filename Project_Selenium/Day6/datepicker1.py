from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support import ui

#selenium4
serv_obj = Service()
driver = webdriver.Edge(service=serv_obj)

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()
time.sleep(5)

driver.switch_to.frame(0) #switch to frame

# driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("08/30/2023")
# time.sleep(5)

#mm/dd/yyyy

year = "2020"
month = "June"
date = "10"

driver.find_element(By.XPATH,"//input[@id='datepicker']").click()

while True:
    mon = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yr = driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text

    if mon==month and yr==year:
        break;
    else:
        #driver.find_element(By.XPATH,"//a[@title='Next']").click()
        driver.find_element(By.XPATH, "//a[@title='Prev']").click()


#date
dates = driver.find_elements(By.XPATH,"//*[@id='ui-datepicker-div']/table/tbody/tr/td/a")

for date in dates:
    if date.text == date:
        date.click()
        time.sleep(5)
        break




