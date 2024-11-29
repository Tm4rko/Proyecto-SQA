from selenium.webdriver.common.by import By

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
        





    