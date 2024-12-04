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
        """self.driver.find_element(By.XPATH, "//a[text()='Entrar']").click()"""
        time.sleep(2)

    def teardown_method(self):
        self.driver.quit()
        print("Prueba visual completada")

    def test_login_miraflores(self):
        sucursal = "Miraflores"
        Login.login_account(self, "clienteb@gmail.com", "123456789a", sucursal)
        dev = Login.sucursal_select(self)
        assert sucursal in dev
        time.sleep(2)

    def test_login_sopocachi(self):
        sucursal = "Sopocachi"
        Login.login_account(self, "clienteb@gmail.com", "123456789a", sucursal)
        dev = Login.sucursal_select(self)
        assert sucursal in dev
        time.sleep(2)

    def test_login__el_alto(self):
        sucursal = "San Pedro"
        Login.login_account(self, "clienteb@gmail.com", "123456789a", sucursal)
        dev = Login.sucursal_select(self)
        assert sucursal in dev
        time.sleep(2)

    def test_login__san_pedro(self):
        sucursal = "El Alto"
        Login.login_account(self, "clienteb@gmail.com", "123456789a", sucursal)
        dev = Login.sucursal_select(self)
        assert sucursal in dev
        time.sleep(2)


    def test_menu(self):
        self.driver.find_element(By.XPATH, "//a").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//a[@id='id-registrate']").click()
        time.sleep(1)
        esperado_registrate = "Crear una nueva cuenta"
        actual_registrate = self.driver.find_element(By.XPATH, "//h3[@class='card-title float-none text-center']").text

        self.driver.find_element(By.XPATH, "//a[@id='id-volver-registro']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//a[@id='id-entrar']").click()
        time.sleep(1)
        esperado_login = "Autenticarse para iniciar sesión"
        actual_login = self.driver.find_element(By.XPATH, "//h3[@class='card-title float-none text-center']").text
        self.driver.find_element(By.XPATH, "//a[@id='id-volver-login']").click()
        time.sleep(1)

        self.driver.find_element(By.XPATH, "//a[@id='id-pedido']").click()
        time.sleep(1)
        esperado_pedido = "Realiza tu Pedido en Línea"
        actual_pedido = self.driver.find_element(By.XPATH, "//h1").text

        self.driver.find_element(By.XPATH, "//a[@id='id-inicio']").click()
        time.sleep(1)
        esperado_inicio = "Nuestro Restaurante"
        actual_inicio = self.driver.find_element(By.XPATH, "//h2[@id='titleHistory']").text

        assert esperado_registrate in actual_registrate, f"LOS VALORES NO COINCIDEN: Actual: {actual_registrate}, Esperado: {esperado_registrate}"
        assert esperado_login in actual_login, f"LOS VALORES NO COINCIDEN: Actual: {actual_login}, Esperado: {esperado_login}"
        assert esperado_pedido in actual_pedido, f"LOS VALORES NO COINCIDEN: Actual: {actual_pedido}, Esperado: {esperado_pedido}"
        assert esperado_inicio in actual_inicio, f"LOS VALORES NO COINCIDEN: Actual: {actual_inicio}, Esperado: {esperado_inicio}"






    
