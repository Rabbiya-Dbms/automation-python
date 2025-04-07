import time
from typing import KeysView

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://fs2.formsite.com/meherpavan/form2/index.html')
browser.maximize_window()
#for scroll down
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
browser.find_element(By.XPATH,"//label[normalize-space()='Sunday']").click()
time.sleep(3)
browser.find_element(By.XPATH,"//label[normalize-space()='Sunday']").click()
time.sleep(3)

#variable for checkboxex
checkboxes = browser.find_elements(By.XPATH,"//input[@type='checkbox']")
#to select all of these checkboxes
for checkbox in checkboxes:
    checkbox.send_keys(Keys.SPACE)
#to check checkboxes count
checked_count = 0

for checkbox in checkboxes:
    if  checkbox.is_selected():
        checked_count +=1  #1 ka increment

expected_checked_count = 7

if checked_count == expected_checked_count:
    print('checkbox count verified')
else:
    print('checkbox count mismatched')
time.sleep(3)
browser.close()


