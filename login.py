from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://staging.ayudarapidapr.com/signin")

# Enter credentials
driver.find_element(By.XPATH, "//input[@type='email']").send_keys("rabbiya+a8@expedey.com")
driver.find_element(By.XPATH, "//input[@type='password']").send_keys("Temp123@")

# Click login using JavaScript (to avoid click interception)
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
driver.execute_script("arguments[0].click();", login_button)

time.sleep(3)  # Give time for the page to load
print("✅ Login Test Completed!")

driver.quit()

