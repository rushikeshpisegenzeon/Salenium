from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Salenium Training\Salenium\Drivers\edgedriver_win64\msedgedriver.exe")
driver = webdriver.Edge(service=serv_obj)
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()

#self

# text_msg=driver.find_element(By.XPATH,"//a[normalize-space()='Indo Count Inds.']/self::a").text
# print(text_msg)

#parent
# text_msg=driver.find_element(By.XPATH,"//a[normalize-space()='Indo Count Inds.']/parent::td").text
# print(text_msg)  #Indo Count Inds.

#child
# childs=driver.find_elements(By.XPATH,"//a[normalize-space()='Indo Count Inds.']/ancestor::tr/child::td").__len__()
# print(childs)

#Ancestor
# ancestor = driver.find_element(By.XPATH,"//a[normalize-space()='Indo Count Inds.']/ancestor::tr").text
# print(ancestor) #Indo Count Inds. A 229.25 233.70 + 1.94

#following
following = driver.find_elements(By.XPATH,"//a[normalize-space()='Indo Count Inds.']/ancestor::tr/following::*").__len__()
print("Number of descendant nodes: ",following)  #Number of descendant nodes:  1801


driver.close()