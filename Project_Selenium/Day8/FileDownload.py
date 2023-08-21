#Mime types --> https://www.sitepoint.com/mime-types-complete-list/
#some additional changes for firefox browser
# ops.set_preference("browser.helperApps.neverAsk.saveToDisk","application/msword")
# ops.set_preference("browser.download.manager.showWhenStarting",False)
# ops.set_preference("browser.download.folderList",2)#0-desktop 1-downloads folder 2-Desired location
# ops.set_preference("browser.download.dir",location)

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
location = os.getcwd() #for getting current working directiory location

def edge_setup():
    from selenium.webdriver.edge.service import Service
    serv_obj = Service()
    #download the file at disired location
    preferences = {"download.default_directory":location} #key value pair
    ops = webdriver.EdgeOptions()
    ops.add_experimental_option("prefs",preferences)



    driver = webdriver.Edge(service=serv_obj,options=ops)
    return driver


driver = edge_setup()
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
driver.maximize_window()
driver.find_element(By.XPATH,"//tbody/tr[1]/td[5]/a[1]").click()
time.sleep(10)