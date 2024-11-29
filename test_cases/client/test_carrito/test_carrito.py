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

    def test_agregar_items_carrito(self):
        Login.login_account("clienteb@gmail.com", "123456789a")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//a[text()='Realiza tu PEDIDO']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//div[@data-bs-target='#productoModal-110']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[@onclick='increaseCount(110, 45.00, 22)']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//button[@onclick="increaseTerm(110, \'medio\')"]').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, '//button[@onclick="increaseGuarnicion(110, 117)"]').click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@id='specification-110']//following-sibling::input").click()
