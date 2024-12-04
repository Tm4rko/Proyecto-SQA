import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestConfiguracion:

    def setup_class(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get('http://localhost/sistemarestaurante/public/admin/configuracion')
        time.sleep(2)

    def teardown_class(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//input[@name='email']").send_keys("Admin@gmail.com")
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys("123456789a")
        driver.find_element(By.XPATH, "//button[@class='btn btn-block btn-flat btn-primary']").click()
        time.sleep(3)

    def test_submit_configuracion(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)

    def test_validacion_final(self):
        print("Prueba completada exitosamente.")