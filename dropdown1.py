from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#we need a driver
driver = webdriver.Firefox()
driver.maximize_window()
login_url = "https://the-internet.herokuapp.com/dropdown"
driver.get(login_url)

#to interact with dd create obj of select class, this fun needs a dd locator
dropdown_element = driver.find_element(By.ID,"dropdown" )
select = Select(dropdown_element)

# select the value by visible text
# select the value by Index
# select the option by using a value

select.select_by_visible_text("Option 2 ")