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

    """def test_agregar_items_carrito(self):
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
    

    def test_items_carrito(self):
        Login.login_account(self, "clienteb@gmail.com", "123456789a", "Miraflores")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//a[text()='Realiza tu PEDIDO']").click()
        time.sleep(1)
        listItemTitle = productos.agregar_producto(self, 1, 110, "medio", 117)
        time.sleep(1)
        listItemTitle1 = productos.agregar_producto(self, 2, 112, "trescuartos", 118)
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//a[@href='vercarrito' and contains(@class, 'btn')]").click()
        time.sleep(1)

        carritoItemTitle = self.driver.find_element(By.XPATH, "//td[@id='idTitleItem110']").text
        carritoItemTitle1 = self.driver.find_element(By.XPATH, "//td[@id='idTitleItem112']").text
        time.sleep(1)
        assert listItemTitle == carritoItemTitle, f"LOS VALORES NO COINCIDEN: Actual: {carritoItemTitle}, Esperado: {listItemTitle}"
        assert listItemTitle1 == carritoItemTitle1, f"LOS VALORES NO COINCIDEN: Actual: {carritoItemTitle1}, Esperado: {listItemTitle1}"
        

    def test_confirmar_carrito(self):
        Login.login_account(self, "clienteb@gmail.com", "123456789a", "Miraflores")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//a[text()='Realiza tu PEDIDO']").click()
        time.sleep(1)
        listItemTitle = productos.agregar_producto(self, 1, 110, "medio", 117)
        time.sleep(1)
        listItemTitle1 = productos.agregar_producto(self, 2, 112, "trescuartos", 118)
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//a[@href='vercarrito' and contains(@class, 'btn')]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//a[@class='btn btn-success']").click()
        time.sleep(1)
        esperado_mensaje = "¡Tu pedido ha sido registrado con éxito!"
        actual_mensaje = self.driver.find_element(By.XPATH, "//div[contains(@class,'alert-dismissible')]").text
        time.sleep(1)
        
        assert esperado_mensaje in actual_mensaje, f"LOS VALORES NO COINCIDEN: Actual: {actual_mensaje}, Esperado: {esperado_mensaje}"
        

    def test_eliminar_item(self):
        Login.login_account(self, "clienteb@gmail.com", "123456789a", "Miraflores")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//a[text()='Realiza tu PEDIDO']").click()
        time.sleep(1)
        listItemTitle = productos.agregar_producto(self, 1, 110, "medio", 117)
        time.sleep(1)
        listItemTitle1 = productos.agregar_producto(self, 2, 112, "trescuartos", 118)
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//td[@id='112']//following-sibling::td//a").click()
        time.sleep(1)
        contador_esperado = 2
        contador_actual = len(self.driver.find_elements(By.XPATH, "//table//tr"))

        assert contador_esperado == contador_actual, f"LOS VALORES NO COINCIDEN: Actual: {contador_actual}, Esperado: {contador_esperado}"
    """

    def test_eliminar_carrito(self):
        productos.login_producto(self)

        self.driver.find_element(By.XPATH, "//a[@href='vercarrito' and contains(@class, 'btn')]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//a[@class='btn btn-outline-danger']").click()
        time.sleep(1)

        esperado_mensaje = "Carrito eliminado correctamente!"
        actual_mensaje = self.driver.find_element(By.XPATH, "//div[@id='success-message']").text
        assert esperado_mensaje in actual_mensaje, f"LOS VALORES NO COINCIDEN: Actual: {actual_mensaje}, Esperado: {esperado_mensaje}"

    """def test_eliminar_item_carrito(self):
        TestLogin.login_producto()

        self.driver.find_element(By.XPATH, "//a[@href='vercarrito' and contains(@class, 'btn')]").click()
        time.sleep(1)
        """







    


        


    



        
