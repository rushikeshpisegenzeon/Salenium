from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time
#selenium4
serv_obj = Service()
driver = webdriver.Edge(service=serv_obj)

driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
driver.maximize_window()
time.sleep(5)

min_slider = driver.find_element(By.XPATH,"//span[1]")
max_slider = driver.find_element(By.XPATH,"//span[2]")

print("Location of slider Before moving ....")
print(min_slider.location) #{'x': 59, 'y': 250}
print(max_slider.location) #{'x': 489, 'y': 250}

act = ActionChains(driver)
act.drag_and_drop_by_offset(min_slider,100,0).perform()
time.sleep(5)

act.drag_and_drop_by_offset(max_slider,-39,0).perform()
time.sleep(5)

print("Location of slider After moving ....")
print(min_slider.location) #{'x': 158, 'y': 250}
print(max_slider.location) #{'x': 450, 'y': 250}