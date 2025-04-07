import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.maximize_window()
url = "https://the-internet.herokuapp.com/javascript_alerts"
browser.get(url)
#alert btn
AlertBtn = browser.find_element(By.XPATH,"//button[normalize-space()='Click for JS Alert']")
AlertBtn.click()


#we need to deal with this alert.
alert = browser.switch_to.alert
alert_text = alert.text
print(alert_text)
time.sleep(3)
#there is a method to handel alert btn
alert.accept()
#alerrt.dismiss() used for cancelling the alert.
#for handling alert with input field:
#alert.send_keys("testing alerts with selenium python")
#alert.accept()
time.sleep(5)



