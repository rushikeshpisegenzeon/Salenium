import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service()
driver = webdriver.Edge(service=serv_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()


checkBoxes=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'checkBoxOption')]")
print(len(checkBoxes))

#approch1
# for i in range(len(checkBoxes)):
#     checkBoxes[i].click()
#
# time.sleep(5)

#approch2
# for checkBox in checkBoxes:
#     checkBox.click()
#
# time.sleep(5)

#approch3  select multiple checkboxes by choice
# for checkBox in checkBoxes:
#     option=checkBox.get_attribute('id')
#     if option == 'checkBoxOption1' or option=='checkBoxOption3':
#         checkBox.click()
# time.sleep(5)

# approch4 select last 2 checkBoxes
for i in range(len(checkBoxes)-2,len(checkBoxes)):
     checkBoxes[i].click()

time.sleep(5)

# clearing all the check boxes
for checkBox in checkBoxes:
    if checkBox.is_selected():
        checkBox.click()
time.sleep(5)



driver.quit()