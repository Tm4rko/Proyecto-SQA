from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

from page_elements.client.login.modulo_login import Login
from page_elements.client.lista_productos.modulo_productos import productos

class TestLogin:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://localhost/sistemarestaurante/public/login")
        time.sleep(2)

    def teardown_method(self):
        self.driver.quit()
        print("Prueba visual completada")

    def test_agregar_items_carrito(self):
        Login.login_account(self, "clienteb@gmail.com", "123456789a", "Miraflores")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//a[text()='Realiza tu PEDIDO']").click()
        time.sleep(1)
        listItemTitle = productos.agregar_producto(self, 1, 110, "medio", 117)
        time.sleep(1)
        listItemTitle1 = productos.agregar_producto(self, 2, 112, "trescuartos", 118)
        time.sleep(1)

        carritoItemTitle = self.driver.find_element(By.XPATH, "//table//td[@id='110']").text
        carritoItemTitle1 = self.driver.find_element(By.XPATH, "//table//td[@id='112']").text

        assert listItemTitle == carritoItemTitle, f"LOS VALORES NO COINCIDEN: Actual: {carritoItemTitle}, Esperado: {listItemTitle}"
        assert listItemTitle1 == carritoItemTitle1, f"LOS VALORES NO COINCIDEN: Actual: {carritoItemTitle1}, Esperado: {listItemTitle1}"
        



        
