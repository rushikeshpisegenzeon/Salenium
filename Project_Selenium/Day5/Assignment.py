import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

serv_obj = Service()
driver = webdriver.Edge(service=serv_obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(5)

# driver.find_element(By.XPATH,"//button[normalize-space()='Confirm Box']").click()
# alt_btn = driver.switch_to.alert
# time.sleep(5)
# alt_btn.accept()
# time.sleep(5)


driver.find_element(By.XPATH,"//input[@id='Wikipedia1_wikipedia-search-input']").send_keys("selenium")
driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(5)

results = driver.find_elements(By.ID,"wikipedia-search-result-link")

for result in results:
    result.find_element(By.TAG_NAME,"a").click()
    time.sleep(5)

window_Ids = driver.window_handles

for id in window_Ids:
    driver.switch_to.window(id)
    print(driver.title+" : " + id )
    driver.switch_to.default_content()

driver.quit()

















