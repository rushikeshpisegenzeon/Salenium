from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

serv_obj = Service("C:\Selenium Training\Salenium\Drivers\edgedriver_win64\msedgedriver.exe")
driver = webdriver.Edge(service=serv_obj)

driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()


#is_displayed()  #is_enabled()

searchBox = driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
print("Display Status : ",searchBox.is_displayed())
print("Enabled Status : ",searchBox.is_enabled())

#is_selected()
rd_male = driver.find_element(By.XPATH,"//input[@id='gender-male']")
print("male radio button ",rd_male.is_selected())

rd_female = driver.find_element(By.XPATH,"//input[@id='gender-female']")
print("female radio button ",rd_female.is_selected())

rd_male.click()
rd_male = driver.find_element(By.XPATH,"//input[@id='gender-male']")
print("male radio button after click ",rd_male.is_selected())
