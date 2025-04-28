from selenium import webdriver
from selenium.webdriver.common.by import By
#execution fast and no interaction error. agar element find hojata hai tw wait k liye nh rukta foran se interact kr leta hai.
driver = webdriver.Chrome()
#implicit wait applied at driver level: 10 sec applicable for every element here this is a dynamic weight. ,max 10 sec
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://www.saucedemo.com/v1/")

driver.find_element(By.ID,"user-name").send_keys("standard_user")

driver.find_element(By.ID,"password").send_keys("secret_sauce")

driver.find_element(By.ID,"login-button").click()

driver.find_element(By.XPATH,"//button[normalize-space()='Open Menu']").click()

driver.find_element(By.XPATH,"//a[@id='logout_sidebar_link']").click()

driver.quit()
