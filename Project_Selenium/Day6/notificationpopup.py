import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

ops = webdriver.EdgeOptions()
ops.add_argument("--disable-notifications")

serv_obj = Service()
driver = webdriver.Edge(service=serv_obj,options=ops)

driver.get("https://whatmylocation.com/")
driver.maximize_window()
time.sleep(5)