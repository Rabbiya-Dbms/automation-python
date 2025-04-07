from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.maximize_window()
browser.get('https://the-internet.herokuapp.com/nested_frames')

#we need to switch to the top frame the middle
#top frame

browser.switch_to.frame("frame-top") # ye top frame ka name hei


#switching to middle frame

browser.switch_to.frame("frame-middle")

#print the value
content = browser.find_element(By.ID, "content").text  #middle frame ki value text m print hojaegi
print("content in middle frame", content)

#switch to default content

browser.switch_to.default_content()

#switch to bottom frame

browser.switch_to.frame("frame-bottom")
#print the value
content_bottom = browser.find_element(By.TAG_NAME, "body").text  #middle frame ki value text m print hojaegi
print("content in bottom frame", content_bottom)
