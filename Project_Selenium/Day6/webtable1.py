# 1) Count number of rows and colums
# 2) Read specific row and column data
# 3) Read all the rows and colums data
# 4) Read data based on condition(List books names whoes author is Mukesh)

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

serv_obj = Service()
driver = webdriver.Edge(service=serv_obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
#time.sleep(5)

# 1) Count number of rows and colums

number_of_rows = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
number_of_columns = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th"))
#
# print("number of rows : ",number_of_rows) #7
# print("number of columns : ",number_of_columns) #4

# 2) Read specific row and column data
# data = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[5]/td[1]").text
# print(data)

# 3) Read all the rows and colums data
# print("Printing all the rows and columns data ....")
# for r in range(2,number_of_rows+1):
#     for c in range(1,number_of_columns+1):
#         data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
#         print(data,end='              ')
#     print()

# 4) Read data based on condition(List books names whoes author is Mukesh)
print("Printing books whoes author is mukesh ....")
for r in range(2,number_of_rows+1):
        authorname = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
        if authorname=="Mukesh":
            bookname = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[1]").text
            print(authorname," ",bookname)


