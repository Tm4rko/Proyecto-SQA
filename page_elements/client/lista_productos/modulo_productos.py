from selenium.webdriver.common.by import By
from page_elements.client.login.modulo_login import Login
import time


class productos:
    def agregar_producto(self, clicks, id_producto, termino_carne, id_guarnicion):
        self.driver.find_element(By.XPATH, f"//div[@data-bs-target='#productoModal-{id_producto}']").click()
        time.sleep(1)
        modalTitle = self.driver.find_element(By.XPATH, f"//h5[@id='productoModalLabel-{id_producto}']").text
        if(clicks > 1):
            for _ in range(clicks - 1):
                self.driver.find_element(By.XPATH, f"//button[contains(@onclick, 'increaseCount({id_producto}')]").click()
                time.sleep(1)
        for _ in range(clicks):
            self.driver.find_element(By.XPATH, f'//button[@onclick="increaseTerm({id_producto}, \'{termino_carne}\')"]').click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, f'//button[@onclick="increaseGuarnicion({id_producto}, {id_guarnicion})"]').click()
            time.sleep(1)
        self.driver.find_element(By.XPATH, f"//input[@id='specification-{id_producto}']//following-sibling::input").click()
        time.sleep(1)
        return modalTitle
    
    def login_producto(self):
        Login.login_account(self, "clienteb@gmail.com", "123456789a", "Miraflores")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//a[text()='Realiza tu PEDIDO']").click()
        time.sleep(1)
        productos.agregar_producto(self, 1, 110, "medio", 117)
        time.sleep(1)
        productos.agregar_producto(self, 2, 112, "trescuartos", 118)
        time.sleep(1)