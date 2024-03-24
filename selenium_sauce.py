# Selenium Python Task:
# 1. Go to URL: https://www.saucedemo.com/
# 2. Log in with standard_user
# 3. Verify login is successful
# 4. Add a product to the cart
# 5. Go to cart and checkout
# 6. Enter name & postal code
# 7. Finish the purchase
# 8. Verify that the purchase is successful
# 8. Go back to homepage
# 9. Log out
# 10. Verify user is logged out successfully

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#import time
driver=webdriver.Firefox()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
#Login
driver.find_element("xpath","(//input[@name='user-name'])").send_keys("standard_user")
driver.find_element("xpath","(//input[@name='password'])").send_keys("secret_sauce")
driver.find_element("xpath","(//input[@id='login-button'])").click()
act_title=driver.title
exp_title="Swag Labs"
if act_title==exp_title:
    print("LOGIN TEST PASS")
else:
    print("LOGIN TEST FAIL")
#Add a product to the cart
driver.find_element("xpath","(//button[@id='add-to-cart-sauce-labs-fleece-jacket'])").click()
#Go to cart and checkout
driver.find_element("xpath","(//a[@class='shopping_cart_link'])").click()
driver.find_element("xpath","(//button[@id='checkout'])").click()
#Enter name & postal code
driver.find_element("xpath","(//input[@id='first-name'])").send_keys("abdc")
driver.find_element("xpath","(//input[@data-test='lastName'])").send_keys("efgh")
driver.find_element("xpath","(//input[@id='postal-code'])").send_keys("1234")
driver.find_element("xpath","(//input[@id='continue'])").click()
#Finish the purchase & verify
driver.find_element("name","finish").click()
act_title=driver.title
exp_title="Swag Labs"
if act_title==exp_title:
    print("PURCHASE TEST PASS")
else:
    print("PURCHASE TEST FAIL")
#Go back to homepage
driver.find_element("xpath","(//button[@id='back-to-products'])").click()
#Logout & Verify
driver.find_element("id","react-burger-menu-btn").click()
driver.find_element("id","logout_sidebar_link").click()
act_title=driver.title
exp_title="Swag Labs"
if act_title==exp_title:
    print("LOGOUT TEST PASS")
else:
    print("LOGOUT TEST FAIL")
driver.close()


