# Incluir acá los test cases para el módulo específico.
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome()
 
driver.maximize_window()

driver.get('http://localhost/sistemarestaurante/public/home')

time.sleep(2)
# Acciones para interactuar con el navegador
#llenar el imput de correo
driver.find_element(By.XPATH, "//input[@name='email']").send_keys("Admin@gmail.com")
#llenar el imput de contraseña
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("123")
#Click contraseña
driver.find_element(By.XPATH, "//button[@class='btn btn-block btn-flat btn-primary']").click()
time.sleep(3)
#Click Roles
driver.find_element(By.XPATH, "(//div[@class='info-box zoomP'])[1]").click()
time.sleep(3)
#Click Roles
driver.find_element(By.XPATH, "(//div[@class='info-box zoomP'])[2]").click()
time.sleep(3)
#Click Roles
driver.find_element(By.XPATH, "(//div[@class='info-box zoomP'])[3]").click()
time.sleep(3)
#Click Roles
driver.find_element(By.XPATH, "(//div[@class='info-box zoomP'])[4]").click()
#Click Nav Item
driver.find_element(By.XPATH, "(//li[@class='nav-item'])[1]").click()
#Click Expandir Menu
driver.find_element(By.XPATH, "(//li[@class='nav-item'])[2]").click()
time.sleep(3)
driver.quit()