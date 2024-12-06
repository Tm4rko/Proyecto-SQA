"""
Antes de ejecutar el test, ejecutar el siguiente comando para instalar las librerías necesarias:

pip install selenium webdriver-manager
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestCategorias:

    def setup_class(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://localhost/sistemarestaurante/public/home')  

    def test_login(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//input[@name='email']").send_keys("admin@gmail.com")
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys("123456789a")

        driver.find_element(By.XPATH, "//button[@class='btn btn-block btn-flat btn-primary']").click()
        time.sleep(2)

        actual = "marko"  
        devuelto = driver.find_element(By.XPATH,"//a[@class='nav-link dropdown-toggle']").text  
        assert actual in devuelto, f"Error en la visualización de la categoria: Se esperaba '{actual}', pero se obtuvo '{devuelto}'"
        time.sleep(2)

     

    def test_navigate_to_categories(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//i[@class='fas fa-fw fa-tags ']//following-sibling::p[contains(text(), 'Categorias Menú')]").click()
        time.sleep(2)

        #en revision


        driver.find_element(By.XPATH, "//i[@class='far fa-fw fa-circle ']//following-sibling::p[contains(text(), 'Listado de Categorias Menú')]").click()
        time.sleep(2)

        actual = "Listado de Categorias Menú"  
        devuelto = driver.find_element(By.XPATH,"//i[@class='far fa-fw fa-circle ']//following-sibling::p[contains(text(), 'Listado de Categorias Menú')]").text    
        assert actual in devuelto, f"Error en la visualización de la categoria: Se esperaba '{actual}', pero se obtuvo '{devuelto}'"
        time.sleep(2)



    def test_create_category(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//a[@class='btn btn-primary']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@class='form-control']").send_keys("Ensaladas")
        time.sleep(2)
        driver.find_element(By.XPATH, "(//input[@class='form-control'])[2]").send_keys("Las ensaladas son parte de ")
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()
        time.sleep(2)

        actual = "Se registró la categoría de manera correcta"
        devuelto = driver.find_element(By.XPATH, "//div[@class='swal2-html-container']").text
        assert actual == devuelto, f"Error: Se esperaba '{actual}', pero se obtuvo '{devuelto}'"
        driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled']").click()
        time.sleep(2)

    def test_edit_category(self):
        driver = self.driver
        driver.find_element(By.XPATH, "(//i[@class='fas fa-pencil'])[5]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@class='form-control']").send_keys("")
        time.sleep(2)
        driver.find_element(By.XPATH, "(//input[@class='form-control'])[2]").send_keys("las categorias")
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        time.sleep(2)

        actual = "Se modifico la categoria de manera correcta"
        devuelto = driver.find_element(By.XPATH, "//div[@class='swal2-html-container']").text
        assert actual == devuelto, f"Error: Se esperaba '{actual}', pero se obtuvo '{devuelto}'"
        driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled']").click()
        time.sleep(2)

    def test_view_category(self):
        driver = self.driver
        driver.find_element(By.XPATH, "(//a[@class='btn btn-info btn-sm'])[5]").click()
        time.sleep(2)

        actual = "Ensaladas"  
        devuelto = driver.find_element(By.XPATH,"//div[@class='form-group']").text  
        assert actual in devuelto, f"Error en la visualización de la categoria: Se esperaba '{actual}', pero se obtuvo '{devuelto}'"  
        driver.find_element(By.XPATH, "//a[@class='btn btn-secondary']").click()
        time.sleep(2)

    def test_delete_category(self):
        driver = self.driver
        driver.find_element(By.XPATH, "(//i[@class='fas fa-trash'])[5]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled swal2-default-outline']").click()
        time.sleep(2)

        actual = "Se eliminó la categoría de manera correcta"
        devuelto = driver.find_element(By.XPATH, "//div[@class='swal2-html-container']").text
        assert actual == devuelto, f"Error: Se esperaba '{actual}', pero se obtuvo '{devuelto}'"
        driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled']").click()
        time.sleep(2)

    def test_complete(self):
        print("Prueba visual completada")

    def teardown_class(self):
        self.driver.quit()
