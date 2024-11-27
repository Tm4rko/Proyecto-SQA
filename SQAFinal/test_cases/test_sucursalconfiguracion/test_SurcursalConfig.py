# Incluir acá los test cases para el módulo específico.
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configuración automática del WebDriver
driver = webdriver.Chrome()
 
# Maximizar la ventana del navegador
driver.maximize_window()
 
# Abrir url en el navegador
driver.get('http://localhost/sistemarestaurante/public/admin/configuracion')
# Acciones para interactuar con el navegador
time.sleep(2)
#llenar el imput de correo
driver.find_element(By.XPATH, "//input[@name='email']").send_keys("Admin@gmail.com")
#llenar el imput de contraseña
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("123")
#Click contraseña
driver.find_element(By.XPATH, "//button[@class='btn btn-block btn-flat btn-primary']").click()
time.sleep(3)

driver.quit()