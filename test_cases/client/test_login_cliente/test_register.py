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
        Login.register(self, nombre, email, celular, direccion, contraseña)

        esperado_nombre = nombre
        actual_nombre = self.driver.find_element(By.XPATH, "//a[@id='navbarDropdown']").text

        assert esperado_nombre in actual_nombre, f"LOS VALORES NO COINCIDEN: Actual: {actual_nombre}, Esperado: {esperado_nombre}"
        

    def test_register_error(self):
        self.driver.find_element(By.XPATH, "//a[@id='id-registrate']").click()
        time.sleep(1)
        nombre = "Juan Prueba"
        email = "prueba@gmail.com"
        celular = "18958965"
        direccion = "Miraflores Av. Busch, C/ #5986"
        contraseña = "1234567"
        Login.register(self, nombre, email, celular, direccion, contraseña)
        esperado_correo = "El valor del campo correo ya está en uso."
        esperado_celular = "El campo celular debe comenzar con 6 o 7 y debe tener 8 dígitos"
        esperado_contraseña = "El campo contraseña debe contener al menos 8 caracteres."

        actual_correo = self.driver.find_element(By.XPATH, "//strong[contains(text(), 'correo')]").text
        actual_celular = self.driver.find_element(By.XPATH, "//strong[contains(text(), 'celular')]").text
        actual_contraseña = self.driver.find_element(By.XPATH, "//strong[contains(text(), 'contraseña')]").text

        assert esperado_correo in actual_correo, f"LOS VALORES NO COINCIDEN: Actual: {actual_correo}, Esperado: {esperado_correo}"
        assert esperado_celular in actual_celular, f"LOS VALORES NO COINCIDEN: Actual: {actual_celular}, Esperado: {esperado_celular}"
        assert esperado_contraseña in actual_contraseña, f"LOS VALORES NO COINCIDEN: Actual: {actual_contraseña}, Esperado: {esperado_contraseña}"
    