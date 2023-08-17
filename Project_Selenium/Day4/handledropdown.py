import time
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj = Service()
driver = webdriver.Edge(service=serv_obj)

# mywait = WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[NoSuchElementException,
#                                                             ElementNotVisibleException,
#                                                             ElementNotSelectableException,Exception])

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(5)
driver.maximize_window()
time.sleep(5)


drpcountry_ele= driver.find_element(By.XPATH,"//select[@id='dropdown-class-example']")
# time.sleep(5)
drpcountry = Select(drpcountry_ele)

# drpcountry_ele = mywait.until(EC.presence_of_element_located((By.XPATH,"//select[@id='input-country']")))
# drpcountry = Select(drpcountry_ele)


#select option from the dropdown

# drpcountry.select_by_visible_text("Option1")
# drpcountry.select_by_value("10")
# drpcountry.select_by_index(13)
# time.sleep(5)

#capture all the options and print them
alloptions = drpcountry.options
print("total number of options: ",len(alloptions))

for option in alloptions:
    print(option.text)