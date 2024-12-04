import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestCategorias:
    

    def setup_class(cls):
        # Configuración del WebDriver
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.maximize_window()
        cls.driver.get('http://localhost/sistemarestaurante/public/admin/categorias')
    
    def teardown_class(cls):
        # Cerrar el navegador después de todas las pruebas
        cls.driver.quit()



    def test_login(self):
        driver = self.driver
        # Iniciar sesión
        driver.find_element(By.XPATH, "//input[@name='email']").send_keys("admin@gmail.com")
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys("123456789a")
        driver.find_element(By.XPATH, "//button[@class='btn btn-block btn-flat btn-primary']").click()
        time.sleep(2)  # Espera explícita para transición
    
    def test_create_category(self):
        driver = self.driver
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
        
        driver.find_element(By.XPATH, "(//input[@class='form-control'])[2]").send_keys("Las ensaladas son parte de una dieta saludable")
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
    
    def test_edit_category(self):
        driver = self.driver
        # Acción "Modificar"
        driver.find_element(By.XPATH, "(//i[@class='fas fa-pencil'])[5]").click()
        time.sleep(2)
        
        driver.find_element(By.XPATH, "//input[@class='form-control']").clear()  # Limpiar el campo de texto
        driver.find_element(By.XPATH, "//input[@class='form-control']").send_keys("Ensaladas Frescas")
        time.sleep(2)

        driver.find_element(By.XPATH, "(//input[@class='form-control'])[2]").clear()  # Limpiar el campo de texto
        driver.find_element(By.XPATH, "(//input[@class='form-control'])[2]").send_keys("Deliciosas y saludables ensaladas frescas")
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
    
    def test_delete_category(self):
        driver = self.driver
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
    
    def test_view_category(self):
        driver = self.driver
        # Acción "Ver"
        driver.find_element(By.XPATH, "(//a[@class='btn btn-info btn-sm'])[5]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[@class='btn btn-secondary']").click()
        time.sleep(2)
        
    def test_complete(self):
        print("Prueba visual completada")

    
