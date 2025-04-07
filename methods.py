import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the driver (use Firefox in this case)
driver = webdriver.Firefox()

# Navigate to the OrangeHRM login page
driver.get('https://opensource-demo.orangehrmlive.com/')

# Wait for the "Forgot your password" link to be clickable
try:
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".oxd-text.oxd-text--p.orangehrm-login-forgot-header"))
    ).click()
except Exception as e:
    print(f"An error occurred: {e}")

# Pause to observe changes
time.sleep(5)

# Go back to the previous page
driver.back()

# Pause again
time.sleep(5)

# Go forward to the next page
driver.forward()

# Pause again
time.sleep(5)

# Refresh the page
driver.refresh()

# Close the browser
driver.quit()

