from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestLogin:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("")
        time.sleep(3)

    def teardowm_method(self):
        self.driver.quit()
        print("Prueba visual completada")

    def testLogin(self):
        self.driver.find_element(By.XPATH, "")