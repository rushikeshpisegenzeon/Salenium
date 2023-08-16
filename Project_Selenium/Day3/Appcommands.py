from selenium import webdriver
from selenium.webdriver.edge.service import Service

serv_obj = Service("C:\Selenium Training\Salenium\Drivers\edgedriver_win64\msedgedriver.exe")
driver = webdriver.Edge(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")

print(driver.title) #OrangeHRM
print(driver.current_url) #https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
print(driver.page_source)

driver.close()