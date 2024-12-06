from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
 
# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
 
options = AppiumOptions()
options.load_capabilities({
"platformName": "Android",
"appium:automationName": "UiAutomator2",
"appium:appPackage": "com.example.restaurantegd",
"appium:appActivity": "com.example.restaurantegd.MainActivity",
"appium:ensureWebviewsHavePages": True,
"appium:nativeWebScreenshot": True,
"appium:newCommandTimeout": 3600,
"appium:connectHardwareKeyboard": True
})
 
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
 
el2 = driver.find_element(by=AppiumBy.ID, value="com.example.restaurantegd:id/txtRegister")
el2.click()
el3 = driver.find_element(by=AppiumBy.ID, value="com.example.restaurantegd:id/etFullName")
el3.send_keys("German")
el4 = driver.find_element(by=AppiumBy.ID, value="com.example.restaurantegd:id/txtEmail")
el4.send_keys("german@gmail.com")
el5 = driver.find_element(by=AppiumBy.ID, value="com.example.restaurantegd:id/txtPassword")
el5.send_keys("Ger12345@")
el6 = driver.find_element(by=AppiumBy.ID, value="com.example.restaurantegd:id/txtPhone")
el6.send_keys("788609425")
el7 = driver.find_element(by=AppiumBy.ID, value="com.example.restaurantegd:id/txtAddress")
el7.send_keys("El Alto")
el8 = driver.find_element(by=AppiumBy.ID, value="com.example.restaurantegd:id/btnRegister")
el8.click()
 
driver.quit()