# Incluir acá los test cases para el módulo específico.
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome()
 
driver.maximize_window()

driver.get('http://localhost/sistemarestaurante/public/login')

time.sleep(2)
# Acciones para interactuar con el navegador
#llenar el imput de correo
driver.find_element(By.XPATH, "//input[@name='email']").send_keys("Admin@gmail.com")
#llenar el imput de contraseña
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("123")

driver.find_element(By.XPATH, "//label[@for='remember']").click()

driver.find_element(By.XPATH, "//button[@class='btn btn-block btn-flat btn-primary']").click()
time.sleep(3)
driver.quit()