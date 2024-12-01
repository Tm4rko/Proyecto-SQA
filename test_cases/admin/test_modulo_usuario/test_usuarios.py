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
driver.get('http://localhost/sistemarestaurante/public/admin/productos')

# Acciones para interactuar con el navegador

driver.find_element(By.XPATH, "//input[@name='email']").send_keys("admin@gmail.com")

driver.find_element(By.XPATH, "//input[@name='password']").send_keys("123456789a")


driver.find_element(By.XPATH, "//button[@class='btn btn-block btn-flat btn-primary']").click()

time.sleep(2)



#crear

driver.find_element(By.XPATH, "//a[@class='btn btn-info btn-sm']").click()

time.sleep(2)



driver.find_element(By.XPATH, "//a[@class='btn btn-secondary']").click()

time.sleep(2)



driver.find_element(By.XPATH, "//a[@class='btn btn-primary']").click()

time.sleep(2)


driver.find_element(By.XPATH, "//select[@class='form-control']//option[text()='Bebidas']").click()

time.sleep(2)


driver.find_element(By.XPATH, "//input[@class='form-control']").send_keys("agua")

time.sleep(2)



driver.find_element(By.XPATH, "//input[@name='precio_venta']").send_keys("6")

time.sleep(7)





driver.find_element(By.XPATH,"//textarea[@name='descripcion']").send_keys("qwertyuXD")


time.sleep(2)



driver.find_element(By.XPATH, "//button[@class ='btn btn-primary']").click()

time.sleep(10)


driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled']").click()
time.sleep(3)


#editar

driver.find_element(By.XPATH, "(//i[@class='fas fa-pencil'])[1]").click()

time.sleep(5)




driver.find_element(By.XPATH, "//select[@class='form-control']//option[text()='Bebidas']").click()

time.sleep(2)


driver.find_element(By.XPATH, "//input[@class='form-control']").send_keys("")

time.sleep(2)



driver.find_element(By.XPATH, "//input[@name='precio_venta']").send_keys("")

time.sleep(7)






driver.find_element(By.XPATH,"//textarea[@name='descripcion']").send_keys("qwertyuXD")


time.sleep(2)


driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

time.sleep(3)



driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled']").click()
time.sleep(3)




#driver.find_element(By.XPATH, "//select[@name='mitabla_length']//option[@value='10']").click()



#buscar:

driver.find_element(By.XPATH, "//input[@class='form-control form-control-sm']").send_keys("agua")

time.sleep(2)



#borrar
driver.find_element(By.XPATH, "(//i[@class='fas fa-trash'])[1]").click()

time.sleep(3)

driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled swal2-default-outline']").click()

time.sleep(3)






driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled']").click()


time.sleep(2)

print("Prueba visual completada")
