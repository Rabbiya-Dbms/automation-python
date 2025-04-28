from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

# Updated URL (remove /v1/)
driver.get("https://www.saucedemo.com/")

# Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Wait for the menu button and click it
wait = WebDriverWait(driver, 10)
menu_button = wait.until(EC.element_to_be_clickable((By.ID, "react-burger-menu-btn")))
menu_button.click()

# Wait for the logout link and click it
logout_link = wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))
logout_link.click()

# Close the browser
driver.quit()
