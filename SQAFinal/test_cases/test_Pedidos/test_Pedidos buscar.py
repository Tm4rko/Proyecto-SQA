from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.maximize_window()

    driver.get('http://localhost/sistemarestaurante/public/admin/pedidos')
    time.sleep(2)

    # Interactuar con el formulario de inicio de sesión
    driver.find_element(By.XPATH, "//input[@name='email']").send_keys("Admin@gmail.com")
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys("123")
    driver.find_element(By.XPATH, "//button[@class='btn btn-block btn-flat btn-primary']").click()
    time.sleep(3)

    # Escribir en el buscador
    driver.find_element(By.XPATH, "//input[@type='search']").send_keys("elo2")

    time.sleep(3)

    print("Prueba completada exitosamente.")



finally:
    driver.quit()