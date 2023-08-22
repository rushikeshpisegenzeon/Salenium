#https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.select import Select

from Salenium.Project_Selenium.Day11 import XLUtils

serv_obj = Service()
driver = webdriver.Edge(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()

file = "C:\\Users\\RPise\\Documents\\DataDriven.xlsx"
rows = XLUtils.getRowCount(file,"Sheet1")

for r in range(2,rows+1):
    #reading data from excel
    princ = XLUtils.readData(file,"Sheet1",r,1)
    rate_of_interest = XLUtils.readData(file,"Sheet1",r,2)
    per_1 = XLUtils.readData(file,"Sheet1",r,3)
    per_2 = XLUtils.readData(file,"Sheet1",r,4)
    frequency = XLUtils.readData(file,"Sheet1",r,5)
    exe_mvalue = XLUtils.readData(file,"Sheet1",r,6)


    #passing data to the application
    driver.find_element(By.XPATH,"//input[@id='principal']").send_keys(princ)
    driver.find_element(By.XPATH,"//input[@id='interest']").send_keys(rate_of_interest)
    driver.find_element(By.XPATH,"//input[@id='tenure']").send_keys(per_1)
    perioddrp = Select(driver.find_element(By.XPATH,"//select[@id='tenurePeriod']"))
    perioddrp.select_by_visible_text(per_2)
    frequencydrp = Select(driver.find_element(By.XPATH,"//select[@id='frequency']"))
    frequencydrp.select_by_visible_text(frequency)
    #clicking the button
    time.sleep(5)
    driver.find_element(By.XPATH,"//img[@src='https://images.moneycontrol.com/images/mf_revamp/btn_calcutate.gif']").click()

    act_mvalue = driver.find_element(By.XPATH,"//span[@id='resp_matval']/strong").text

    #validation
    if float(exe_mvalue)==float(act_mvalue):
        print("test passed")
        XLUtils.writeData(file,"Sheet1",r,8,"Passed")
        XLUtils.fillGreenColor(file,"Sheet1",r,8)
    else:
        print("test failed")
        XLUtils.writeData(file, "Sheet1", r, 8, "Failed")
        XLUtils.fillRedColor(file, "Sheet1", r, 8)
    driver.find_element(By.XPATH,"//img[@class='PL5']").click()

driver.close()
