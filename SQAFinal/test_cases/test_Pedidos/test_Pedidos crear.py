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

    # Abrir el formulario para crear un nuevo pedido
    driver.find_element(By.XPATH, "//div[@class='card-tools']").click()
    time.sleep(3)

    # Seleccionar categoría
    categoria_dropdown = driver.find_element(By.XPATH, "//select[@name='categoria_id']").click()
    driver.find_element(By.XPATH, "//option[@value='7']").click()

    # Completar los campos del formulario
    driver.find_element(By.XPATH, "//input[@type='text']").send_keys("COCA QUINA")
    driver.find_element(By.XPATH, "//input[@name='precio_venta']").send_keys("11")
    driver.find_element(By.XPATH, "//textarea[@name='descripcion']").send_keys("Orgullosamente Boliviana")
    time.sleep(3)
    # Subir el archivo
    ruta_logo = "C:\\Users\\LARA\\Desktop\\SQA test\\img2.jpg"
    driver.find_element(By.XPATH, "//input[@name='imagen']").send_keys(ruta_logo)
    time.sleep(4)
    # Enviar el formulario
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(3)

    print("Prueba completada exitosamente.")



finally:
    driver.quit()