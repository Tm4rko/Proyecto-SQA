 # Login exitoso

options = AppiumOptions()
options.load_capabilities({
	"platformName": "Android",
	"appium:automationName": "UiAutomator2",
	"appium:appPackage": "com.example.restaurantegd",
	"appium:appActivity": "com.example.restaurantegd.MainActivity",
	"appium:ensureWebviewsHavePages": True,
	"appium:nativeWebScreenshot": True,
	"appium:newCommandTimeout": 3600,
	"appium:connectHardwareKeyboard": True})
 
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
 
el1 = driver.find_element(by=AppiumBy.ID, value="com.example.restaurantegd:id/etEmail")
el1.send_keys("nataniel@gmail.com")
el2 = driver.find_element(by=AppiumBy.ID, value="com.example.restaurantegd:id/etPassword")
el2.send_keys("Nat12345@")
el3 = driver.find_element(by=AppiumBy.ID, value="com.example.restaurantegd:id/btnLogin")
el3.click()
 
driver.quit()