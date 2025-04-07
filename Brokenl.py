from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import time

url = "https://jqueryui.com/"

# Initialize the WebDriver with retry logic for handling intermittent issues
try:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)  # Open URL

    # Get all links on the page
    all_links = driver.find_elements(By.TAG_NAME, 'a')
    print(f"Total number of links on the page: {len(all_links)}")

except WebDriverException as e:
    print(f"Error occurred: {e}")

finally:
    # Close the driver after a short delay
    time.sleep(2)
    driver.quit()
