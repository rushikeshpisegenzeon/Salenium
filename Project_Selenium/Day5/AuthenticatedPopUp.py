import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service()
driver = webdriver.Edge(service=serv_obj)
time.sleep(5)
#inject username and password and by pass it
driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.maximize_window()
time.sleep(5)
