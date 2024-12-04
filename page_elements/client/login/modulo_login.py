from selenium.webdriver.common.by import By
import time

class Login:
    def login_account(self, email, password, sucursal):
        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys(email)
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        self.driver.find_element(By.XPATH, f"//label[text()='{sucursal}']").click()
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()


    def sucursal_select(self):
        devuelto = self.driver.find_element(By.XPATH, "//span[contains(@class, 'nav-link')]").text
        return devuelto
    

    def register(self, nombre, email, celular, direccion, contraseña):
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
        





    