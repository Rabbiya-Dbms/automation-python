from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

# Initialize the driver
driver = webdriver.Firefox()
driver.maximize_window()

# Open the target URL
driver.get("https://the-internet.herokuapp.com/dropdown")

# Find the dropdown element
dropdown_element = driver.find_element(By.ID, "dropdown")
target_value = "Option 2"
select = Select(dropdown_element)

for option in select.options:
    if option.text == target_value:
        option.click()
        print(f"selected option i s{target_value}")
        break
    else:
        print(f"option '{target_value}' not found")

#select = Select(dropdown_element)

#test case to verify dropdown options count
#option_count = len(select.options)

#expected_count = 5

#if option_count ==  expected_count:
  #  print("testcse passed count is correct")

#else:
   # print("testcase failed count is incorrect")


    

# Select the option by visible text (remove any extra spaces)
#select.select_by_visible_text("Option 2".strip())
#select.select_by_index(1)
#select.select_by_value("2") #in string form based on attribute


# Wait for a few seconds to see the selection before closing
time.sleep(3)

# Close the browser
driver.quit()


#how to interact with dd
#how to use select class
#how to use 3 diff methods
#select by value,index,visible text
#how to count the dropdown values
#loop the dd value and if desired value found select that value