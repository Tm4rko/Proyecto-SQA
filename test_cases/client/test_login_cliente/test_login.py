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
        sucursal = "Miraflores"
        Login.login_account(self, "clienteb@gmail.com", "123456789a", sucursal)
        dev = Login.sucursal_select(self, sucursal)
        assert sucursal in dev
        time.sleep(2)

    def test_login_sopocachi(self):
        sucursal = "Sopocachi"
        Login.login_account(self, "clienteb@gmail.com", "123456789a", sucursal)
        dev = Login.sucursal_select(self, sucursal)
        assert sucursal in dev
        time.sleep(2)

    def test_login__el_alto(self):
        sucursal = "San Pedro"
        Login.login_account(self, "clienteb@gmail.com", "123456789a", sucursal)
        dev = Login.sucursal_select(self, sucursal)
        assert sucursal in dev
        time.sleep(2)

    def test_login__san_pedro(self):
        sucursal = "El Alto"
        Login.login_account(self, "clienteb@gmail.com", "123456789a", sucursal)
        dev = Login.sucursal_select(self, sucursal)
        assert sucursal in dev
        time.sleep(2)





    
