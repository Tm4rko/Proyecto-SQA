from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

from page_elements.client.login.modulo_login import Login

class TestLogin:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://localhost/sistemarestaurante/public/login")
        time.sleep(3)

    def teardowm_method(self):
        self.driver.quit()
        print("Prueba visual completada")

    def testLogin(self):
        Login.login_account(self, "cliente2@gmail.com", "123456789a")
        time.sleep(2)