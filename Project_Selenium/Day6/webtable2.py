from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time
#selenium4
serv_obj = Service()
driver = webdriver.Edge(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
time.sleep(5)

driver.find_element(By.NAME,"username").send_keys("Admin")
time.sleep(5)

driver.find_element(By.NAME,"password").send_keys("admin123")
time.sleep(5)

driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
time.sleep(5)

driver.find_element(By.XPATH,"//li[1]//a[1]//span[1]").click()
time.sleep(5)
driver.find_element(By.XPATH,"//span[normalize-space()='User Management']").click()
time.sleep(5)
driver.find_element(By.XPATH,"//a[normalize-space()='Users']").click()
time.sleep(5)

#total rows
rows = len(driver.find_elements(By.XPATH,"//div[@role='rowgroup']/div"))
print("total number of rows in a table: ",rows)
time.sleep(5)

for r in range(1,rows+1):
    status = driver.find_element(By.XPATH,"//div[@role='rowgroup']/div[1]/div["+str(r)+"]/div[1]/div[2]/div[3]/div[1]/div[2]").text
    time.sleep(5)
    print(status)

#  //body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]
#  //body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]

#//div[@role='rowgroup']/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]