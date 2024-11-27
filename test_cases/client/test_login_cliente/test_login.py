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

    def testLogin(self):
        actual = "Miraflores"

        Login.login_account(self, "cliente2@gmail.com", "123456789a")
        time.sleep(2)
        self.driver.find_element(By.XPATH, f"//label[text()='{actual}']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(1)

        devuelto = self.driver.find_element(By.XPATH, "//span[contains(@class, 'nav-link')]").text

        assert actual in devuelto
        
    
