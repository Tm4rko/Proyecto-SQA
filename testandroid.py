# resgitro exitoso  
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
 
el1 = driver.find_element(by=AppiumBy.ID, value="com.example.restaurantegd:id/txtRegister")
el1.click()
el2 = driver.find_element(by=AppiumBy.ID, value="com.example.restaurantegd:id/etFullName")
el2.send_keys("German Poma")
el3 = driver.find_element(by=AppiumBy.ID, value="com.example.restaurantegd:id/txtEmail")
el3.send_keys("german@gmail.com")
el4 = driver.find_element(by=AppiumBy.ID, value="com.example.restaurantegd:id/txtPassword")
el4.send_keys("Ger12345@")
el5 = driver.find_element(by=AppiumBy.ID, value="com.example.restaurantegd:id/txtPhone")
el5.send_keys("78860942")
el6 = driver.find_element(by=AppiumBy.ID, value="com.example.restaurantegd:id/txtAddress")
el6.send_keys("El Alto")
el7 = driver.find_element(by=AppiumBy.ID, value="com.example.restaurantegd:id/btnRegister")
el7.click()
el7.click()
 
driver.quit()