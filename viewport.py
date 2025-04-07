import time

from selenium import webdriver

#create an array for all viewports
viewports = [(1024,786),(786,1024),(375,667),(414,896)]

driver = webdriver.Chrome()
driver.get('https://www.google.com/')

#driver.set_window_size(786,1024)
#time.sleep(3)
#to iterate each array value
try:
    for width,height in viewports:
        driver.set_window_size(width, height)
        time.sleep(3)

finally:
    driver.close()

