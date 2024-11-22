from selenium.webdriver.common.by import By

class Login:
    def login_account(self, email, password):
        self.driver.find_element(By.XPATH, "//input[@name='email']").send_keys(email)
        self.driver.find_element(By.XPATH, "//input[@name='password']").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()