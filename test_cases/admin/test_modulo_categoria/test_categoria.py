"""
Antes de ejecutar el test, ejecutar el siguiente comando para instalar las librerías necesarias:

pip install selenium webdriver-manager
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome()  


driver.maximize_window()


driver.get('http://localhost/sistemarestaurante/public/admin/categorias')

# Iniciar sesión
driver.find_element(By.XPATH, "//input[@name='email']").send_keys("admin@gmail.com")
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("123456789a")
driver.find_element(By.XPATH, "//button[@class='btn btn-block btn-flat btn-primary']").click()
time.sleep(2)

# Acción "Ver"
driver.find_element(By.XPATH, "//a[@class='btn btn-info btn-sm']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[@class='btn btn-secondary']").click()
time.sleep(2)

# Acción "Crear"
driver.find_element(By.XPATH, "//a[@class='btn btn-primary']").click()
time.sleep(2)

driver.find_element(By.XPATH, "//input[@class='form-control']").send_keys("Ensaladas")
time.sleep(2)

driver.find_element(By.XPATH, "(//input[@class='form-control'])[2]").send_keys("Las ensaladas son parte de ")
time.sleep(2)

driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()
time.sleep(6)

# Validar creación
actual = "Se registró la categoría de manera correcta"
devuelto = driver.find_element(By.XPATH, "//div[@class='swal2-html-container']").text
assert actual == devuelto, f"Error: Se esperaba '{actual}', pero se obtuvo '{devuelto}'"
print(f"Mensaje de creación: {devuelto}")
driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled']").click()
time.sleep(2)

# Acción "Modificar"
driver.find_element(By.XPATH, "(//i[@class='fas fa-pencil'])[5]").click()
time.sleep(2)

driver.find_element(By.XPATH, "//input[@class='form-control']").send_keys("")
time.sleep(2)

driver.find_element(By.XPATH, "(//input[@class='form-control'])[2]").send_keys("las categorias")
time.sleep(2)

driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
time.sleep(6)

# Validar modificación
actual = "Se modifico la categoria de manera correcta"
devuelto = driver.find_element(By.XPATH, "//div[@class='swal2-html-container']").text
assert actual == devuelto, f"Error: Se esperaba '{actual}', pero se obtuvo '{devuelto}'"
print(f"Mensaje de modificación: {devuelto}")
driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled']").click()
time.sleep(2)

# Acción "Ver"
driver.find_element(By.XPATH, "(//a[@class='btn btn-info btn-sm'])[5]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[@class='btn btn-secondary']").click()
time.sleep(2)

# Acción "Borrar"
driver.find_element(By.XPATH, "(//i[@class='fas fa-trash'])[5]").click()
time.sleep(2)

driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled swal2-default-outline']").click()
time.sleep(3)

# Validar eliminación
actual = "Se eliminó la categoría de manera correcta"
devuelto = driver.find_element(By.XPATH, "//div[@class='swal2-html-container']").text
assert actual == devuelto, f"Error: Se esperaba '{actual}', pero se obtuvo '{devuelto}'"
print(f"Mensaje de eliminación: {devuelto}")


driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled']").click()
time.sleep(2)

# Cerrar navegador
driver.quit()

print("Prueba visual completada")
