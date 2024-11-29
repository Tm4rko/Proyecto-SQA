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

    def test_login_miraflores(self):
        Login.login_account(self, "clienteb@gmail.com", "123456789a", "Miraflores")
        time.sleep(2)

    def test_login_sopocachi(self):
        Login.login_account(self, "clienteb@gmail.com", "123456789a", "Sopocachi")
        time.sleep(2)

    def test_login__el_alto(self):
        Login.login_account(self, "clienteb@gmail.com", "123456789a", "El Alto")
        time.sleep(2)

    def test_login__san_pedro(self):
        Login.login_account(self, "clienteb@gmail.com", "123456789a", "San Pedro")
        time.sleep(2)





    
