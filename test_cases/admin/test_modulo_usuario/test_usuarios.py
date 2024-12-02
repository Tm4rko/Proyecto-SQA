"""
Antes de ejecutar el test, ejecutar el siguiente comando para instalar la libreria necesaria

pip install selenium webdriver-manager
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configuración automática del WebDriver
driver = webdriver.Chrome()

# Maximizar la ventana del navegador
driver.maximize_window()

# Abrir url en el navegador
driver.get('http://localhost/sistemarestaurante/public/home')

# Acciones para interactuar con el navegador

driver.find_element(By.XPATH, "//input[@name='email']").send_keys("admin@gmail.com")

driver.find_element(By.XPATH, "//input[@name='password']").send_keys("123456789a")


driver.find_element(By.XPATH, "//button[@class='btn btn-block btn-flat btn-primary']").click()

time.sleep(2)


driver.find_element(By.XPATH, "//i[@class='fas fa-fw fa-users ']//following-sibling::p[contains(text(), 'Usuarios')]").click()

time.sleep(2)


driver.find_element(By.XPATH, "//i[@class='far fa-fw fa-circle ']//following-sibling::p[contains(text(), 'Usuarios')]").click()
 
time.sleep(2)

#ver

driver.find_element(By.XPATH, "//a[@class='btn btn-info btn-sm']").click()

time.sleep(2)



driver.find_element(By.XPATH, "//a[@class='btn btn-secondary']").click()

time.sleep(2)

#crear


driver.find_element(By.XPATH, "//a[@class='btn btn-primary']").click()

time.sleep(2)



driver.find_element(By.XPATH, "//select[@class='form-control']").send_keys("Cliente")

time.sleep(2)



driver.find_element(By.XPATH, "//input[@class='form-control']").send_keys("Juan Perez")

time.sleep(2)


driver.find_element(By.XPATH, "//input[@name='email']").send_keys("JP321@gmail.com")

time.sleep(2)


driver.find_element(By.XPATH, "//input[@name='celular']").send_keys("68047689")

time.sleep(2)


driver.find_element(By.XPATH, "//input[@name='direccion']").send_keys("Avenida 16 de Julio")

time.sleep(2)


driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Qwerty123--")

time.sleep(2)

driver.find_element(By.XPATH, "//input[@name='password_confirmation']").send_keys("Qwerty123--")

time.sleep(3)

driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()

time.sleep(10)



#validar 
actual = "Se registro al usuario de manera correcta"
devuelto = driver.find_element(By.XPATH, "//div[@class='swal2-html-container']").text
assert actual == devuelto, f"Error: Se esperaba '{actual}', pero se obtuvo '{devuelto}'"
print(f"Mensaje de eliminación: {devuelto}")
 
driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled']").click()
time.sleep(2)





#redordatorio: cambiar la modificacion de juan perez y cambiar la cantidad de usuarios:


driver.find_element(By.XPATH, "(//a[@class='page-link'])[4]").click()
time.sleep(2)


#-----------------------------------------------------------------

#edit
driver.find_element(By.XPATH, "(//a[@class='btn btn-success btn-sm'])[4]").click()

time.sleep(3)



driver.find_element(By.XPATH, "//select[@class='form-control']").send_keys("")

time.sleep(2)



driver.find_element(By.XPATH, "//input[@class='form-control']").send_keys("")

time.sleep(2)


driver.find_element(By.XPATH, "//input[@name='email']").send_keys("")

time.sleep(2)


driver.find_element(By.XPATH, "//input[@name='celular']").send_keys("")

time.sleep(2)


driver.find_element(By.XPATH, "//input[@name='direccion']").send_keys("")

time.sleep(2)


driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Qwerty123--XD")

time.sleep(2)

driver.find_element(By.XPATH, "//input[@name='password_confirmation']").send_keys("Qwerty123--XD")

time.sleep(3)

driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

time.sleep(3)


#validar modificacion
actual = "Se modifico al usuario de manera correcta"
devuelto = driver.find_element(By.XPATH, "//div[@class='swal2-html-container']").text
assert actual == devuelto, f"Error: Se esperaba '{actual}', pero se obtuvo '{devuelto}'"
print(f"Mensaje de eliminación: {devuelto}")
 

driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled']").click()

time.sleep(3)


#ver listas:------------------------------------------------------------------------------------

driver.find_element(By.XPATH, "//select[@class='custom-select custom-select-sm form-control form-control-sm']//option[@value='10']").click()

time.sleep(5)


driver.find_element(By.XPATH, "//select[@class='custom-select custom-select-sm form-control form-control-sm']//option[@value='25']").click()

time.sleep(5)
 
 
driver.find_element(By.XPATH, "//select[@class='custom-select custom-select-sm form-control form-control-sm']//option[@value='10']").click()

time.sleep(5)
 
 #-----------------------------------------------------------------------------------------------------


#buscar:
 
driver.find_element(By.XPATH, "//input[@class='form-control form-control-sm']").send_keys("Juan Perez")
 
time.sleep(2)
 
 
 
#borrar
driver.find_element(By.XPATH, "(//i[@class='fas fa-trash'])[1]").click()
 
time.sleep(3)
 
driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled swal2-default-outline']").click()
 
time.sleep(3)
 
 
 
 
#validar eliminacion
actual = "Se eliminó el usuario de manera correcta"
devuelto = driver.find_element(By.XPATH, "//div[@class='swal2-html-container']").text
assert actual == devuelto, f"Error: Se esperaba '{actual}', pero se obtuvo '{devuelto}'"
print(f"Mensaje de eliminación: {devuelto}")
 
driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled']").click()

 
 
time.sleep(2)
 
 
 
 
 
 
 
 
driver.quit()
 
 
 
print("Prueba visual completada")
 
 
