'''
Created on Mar 27, 2022

@author: Minarni Debora Harahap
'''

from selenium import webdriver
import time

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
password.send_keys("password123#")

# Submit the Form
submit_form = driver.find_element_by_id("loginbutton")
submit_form.click()

expectedElement = "//div[contains(text(), 'Username atau password salah. Mohon coba lagi.')]"

# Delay 1 second, waiting for the error message appears
time.sleep(1)

if driver.find_element_by_xpath(expectedElement):
    print("Pass")
else:
    print("Fail")

# Close the Browser
driver.close()