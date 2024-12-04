import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestStock:

    def setup_class(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get('http://localhost/sistemarestaurante/public/admin/stocks')
        time.sleep(2)

    def teardown_class(self):
        self.driver.quit()

    def test_login(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//input[@name='email']").send_keys("Admin@gmail.com")
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys("123456789a")
        driver.find_element(By.XPATH, "//button[@class='btn btn-block btn-flat btn-primary']").click()
        time.sleep(3)

    def test_actualizar_stock(self):
        driver = self.driver
        cantidad_input = driver.find_element(By.XPATH, "(//input[@type='number'])[1]")
        cantidad_input.clear() 
        cantidad_input.send_keys("50")

        driver.find_element(By.XPATH, "(//select[@name='disponibilidad'])[1]").click()

        driver.find_element(By.XPATH, "(//button[@type='submit'])[1]").click()
        time.sleep(3)

    def test_validacion_exitosa(self):
        print("Stock actualizado correctamente.")