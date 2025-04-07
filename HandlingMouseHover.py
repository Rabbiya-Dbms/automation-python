from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
browser.maximize_window()
url = "https://demo.automationtesting.in/Datepicker.html"
browser.get(url)

actions = ActionChains(browser)

hover_element = browser.find_element(By.XPATH," //a[normalize-space()='SwitchTo']")
actions.move_to_element(hover_element).perform()
time.sleep(5)
flink = browser.find_element(By.XPATH,"//a[normalize-space()='Frames']")
flink.click()
time.sleep(5)

