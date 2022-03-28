'''
Created on Mar 27, 2022

@author: Minarni Debora Harahap
'''

from selenium import webdriver
import time
from _ast import If

# Initialize the Url
url = "https://stockbit.com/#/login"

driver = webdriver.Firefox()
driver.get(url)
driver.maximize_window()

# Find Email and Fill Email
email = driver.find_element_by_id("username")
email.send_keys("minarnidebora")

# Find Password and Fill Password
password = driver.find_element_by_id("password")
password.send_keys("Password123#")

# Submit the Form
submit_form = driver.find_element_by_id("loginbutton")
submit_form.click()

# Delay 5 seconds, wait for Redirecting to Homepage
time.sleep(30)

currentUrl = driver.current_url
expectedUrl = "https://stockbit.com/#/stream"

if currentUrl == expectedUrl:
    print("Pass")
else:
    print("Fail")
    
# Close the Browser
driver.close()