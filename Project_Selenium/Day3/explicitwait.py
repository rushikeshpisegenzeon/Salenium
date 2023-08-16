from selenium import webdriver
from selenium.common import ElementNotSelectableException, ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

# serv_obj = Service("C:\Selenium Training\Salenium\Drivers\edgedriver_win64\msedgedriver.exe")
serv_obj = Service()
driver = webdriver.Edge(service=serv_obj)

#explicit wait declaration
# mywait = WebDriverWait(driver,10)  #Basic syntax
mywait = WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[NoSuchElementException,
                                                            ElementNotVisibleException,
                                                            ElementNotSelectableException,Exception])

driver.get("https://www.google.com")
driver.maximize_window()

searchBox = driver.find_element(By.XPATH,"//textarea[@id='APjFqb']")
searchBox.send_keys("Selenium")
searchBox.submit()

searchlink=mywait.until(EC.presence_of_element_located((By.XPATH,"//h3[normalize-space()='Selenium']")))
searchlink.click()


driver.quit()
