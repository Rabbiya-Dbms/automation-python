from selenium import webdriver
from selenium.webdriver.common.by import By

url ="https://jqueryui.com/"

#we need a driver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)  #open url

#get all links must be more than 1 link

all_links = driver.find_elements(By.TAG_NAME, 'a')
print(f"Total num of links on the page: {len(all_links)}")

