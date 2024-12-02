from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

from page_elements.client.login.modulo_login import Login

class TestRegister:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://localhost/sistemarestaurante/public")
        """self.driver.find_element(By.XPATH, "//a[text()='Entrar']").click()"""
        time.sleep(2)

    def teardown_method(self):
        self.driver.quit()
        print("Prueba visual completada")

    def test_register(self):
        self.driver.find_element(By.XPATH, "//a[@id='id-registrate']").click()
        time.sleep(1)

        nombre = "Juan Prueba"
        email = "prueba@gmail.com"
        celular = "78958965"
        direccion = "Miraflores Av. Busch, C/ #5986"
        contraseña = "123456789a"
        self.driver.find_element(By.XPATH, "//input[@name='name']").send_keys(nombre)
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys(email)
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@name='celular']").send_keys(celular)
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@name='direccion']").send_keys(direccion)
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(contraseña)
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@name='password_confirmation']").send_keys(contraseña)
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(1)
        esperado_nombre = nombre
        actual_nombre = self.driver.find_element(By.XPATH, "//a[@id='navbarDropdown']").text

        assert esperado_nombre in actual_nombre, f"LOS VALORES NO COINCIDEN: Actual: {actual_nombre}, Esperado: {esperado_nombre}"

    