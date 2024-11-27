from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configuración automática del WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.maximize_window()
    
    driver.get('http://localhost/sistemarestaurante/public/crear-sucursal')
    time.sleep(2)

    # Interactuar con los elementos de la página
    driver.find_element(By.XPATH, "//input[@name='email']").send_keys("Admin@gmail.com")
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys("123")
    driver.find_element(By.XPATH, "//button[@class='btn btn-block btn-flat btn-primary']").click()
    time.sleep(3)

    # Subir archivo 
    ruta_logo = "C:\\Users\\LARA\\Desktop\\SQA test\\img.jpeg"
    driver.find_element(By.XPATH, "//input[@name='logo']").send_keys(ruta_logo)

    # Completar los otros campos del formulario
    driver.find_element(By.XPATH, "//input[@name='nombre_sucursal']").send_keys("Kenko")
    driver.find_element(By.XPATH, "//input[@name='nit']").send_keys("346312543")
    driver.find_element(By.XPATH, "//input[@name='telefono']").send_keys("77352348")
    driver.find_element(By.XPATH, "//input[@name='correo']").send_keys("Kenko@gmail.com")
    driver.find_element(By.XPATH, "//input[@name='direccion']").send_keys("Kenko calle 5")

    # Crear sucursal
    driver.find_element(By.XPATH, "//button[text()='Crear Sucursal']").click()
    time.sleep(6)

    print("Prueba completada exitosamente.")

except Exception as e:
    print(f"Se produjo un error: {e}")

finally:
    driver.quit()