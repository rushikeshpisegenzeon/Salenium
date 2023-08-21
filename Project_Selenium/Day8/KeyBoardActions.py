# Ctrl+A
# Ctrl+C
# Tab
# Ctrl+V

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time
#selenium4
serv_obj = Service()
driver = webdriver.Edge(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://text-compare.com/")
driver.maximize_window()

input1 = driver.find_element(By.XPATH,"//textarea[@id='inputText1']")
input2 = driver.find_element(By.XPATH,"//textarea[@id='inputText2']")

input1.send_keys("welcome to selenium")

act = ActionChains(driver)

#input1 ---> Ctrl+A Select the text

act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

#input1 ---> Ctrl+C copy the text

act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

#Tab key to navigate to input2(second)
act.send_keys(Keys.TAB).perform()

#input2 ---> Ctrl+V paste the text
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
time.sleep(5)



