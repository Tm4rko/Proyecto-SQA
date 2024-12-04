import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestSucursal:

    def setup_class(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.driver.get('http://localhost/sistemarestaurante/public/crear-sucursal')
        time.sleep(2)

    def teardown_class(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//input[@name='email']").send_keys("Admin@gmail.com")
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys("123456789a")
        driver.find_element(By.XPATH, "//button[@class='btn btn-block btn-flat btn-primary']").click()
        time.sleep(3)

    def test_crear_sucursal(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//input[@name='nombre_sucursal']").send_keys("Kenko")
        driver.find_element(By.XPATH, "//input[@name='nit']").send_keys("346312543")
        driver.find_element(By.XPATH, "//input[@name='telefono']").send_keys("77352348")
        driver.find_element(By.XPATH, "//input[@name='correo']").send_keys("Kenko4@gmail.com")
        driver.find_element(By.XPATH, "//input[@name='direccion']").send_keys("Kenko calle 8")

        driver.find_element(By.XPATH, "//button[text()='Crear Sucursal']").click()
        time.sleep(3)

    def test_validacion_final(self):
        print("Prueba completada exitosamente.")