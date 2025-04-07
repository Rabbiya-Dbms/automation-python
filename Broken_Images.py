from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

# Initialize the Firefox browser
browser = webdriver.Firefox()
browser.get("https://the-internet.herokuapp.com/broken_images")
browser.maximize_window()

# Find all the images on the page
images = browser.find_elements(By.TAG_NAME, "img")
# List to store broken image URLs
broken_images = []

#loop through each img
for image in images:
    src = image.get_attribute("src")
    if src:
        #using req.get to make an http req and chk the response
        response = requests.get(src)
        if response.status_code != 200:
            broken_images.append(src)
            print(f"broken img found")

#output the list of broken img's

if broken_images:
    print("list of broken images:")
    for broken_image in broken_images:
        print(broken_image)

else:
    print("no broken img found")





