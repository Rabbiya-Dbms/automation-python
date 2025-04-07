import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

csv_file = "C:/Users/hp/Desktop/login.csv"
df = pd.read_csv(csv_file)

username = df.loc[0, "username"]
password = df.loc[0, "password"]

print(f"login with username: {username}")

login_url = "https://practicetestautomation.com/practice-test-login/"

driver = webdriver.Chrome()
driver.get(login_url)
driver.maximize_window()

uname = driver.find_element(By.NAME,"username")
pwd = driver.find_element(By.NAME,"password")
loginbtn = driver.find_element(By.XPATH,"//button[@id='submit']")

uname.clear()
uname.send_keys(username)
pwd.clear()
pwd.send_keys(password)
loginbtn.click()



