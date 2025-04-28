import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()  #obj hai aargument pass karna hai
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
time.sleep(5)
driver.get("https://www.google.co.uk/")

