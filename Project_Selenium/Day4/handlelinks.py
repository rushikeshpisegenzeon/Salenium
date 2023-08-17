from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service()
driver = webdriver.Edge(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

#click on link
# driver.find_element(By.XPATH,"//a[@title='Show products in category Digital downloads'][normalize-space()='Digital downloads']").click()

#find number of links in page
links = driver.find_elements(By.TAG_NAME,'a')
print("total number of links: ",len(links))

#print all the link names

for link in links:
    print(link.text)

