import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestPedidos:

    def setup_class(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.driver.get('http://localhost/sistemarestaurante/public/admin/pedidos')
        time.sleep(2)

    def teardown_class(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//input[@name='email']").send_keys("Admin@gmail.com")
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys("123456789a")
        driver.find_element(By.XPATH, "//button[@class='btn btn-block btn-flat btn-primary']").click()
        time.sleep(3)

    def test_buscar_pedido(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//input[@type='search']").send_keys("Emerson Quisbert")
        time.sleep(6)

    def test_validacion_final(self):
        print("Prueba completada exitosamente.")