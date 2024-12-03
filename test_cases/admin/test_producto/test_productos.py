import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestProductos:
    
   
    def setup_class(self):
        # Configuración del WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get('http://localhost/sistemarestaurante/public/home')  # Cambia la URL si es necesario

   

    def test_login(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//input[@name='email']").send_keys("admin@gmail.com")
        driver.find_element(By.XPATH, "//input[@name='password']").send_keys("123456789a")
        driver.find_element(By.XPATH, "//button[@class='btn btn-block btn-flat btn-primary']").click()
        time.sleep(2)

    def test_navigate_to_products(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//i[@class='fas fa-fw fa-list ']//following-sibling::p[contains(text(), 'Productos')]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//i[@class='far fa-fw fa-circle ']//following-sibling::p[contains(text(), 'Productos')]").click()
        time.sleep(2)

    def test_create_product(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//a[@class='btn btn-primary']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//select[@class='form-control']//option[text()='Bebidas']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@class='form-control']").send_keys("agua vital")
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@name='precio_venta']").send_keys("6")
        time.sleep(2)
        # Subir archivo 
        ruta_logo = "C:\\Users\\PC\\Desktop\\applio\\pepsi.jpg"
        driver.find_element(By.XPATH, "//input[@name='imagen']").send_keys(ruta_logo)


        time.sleep(2)
        driver.find_element(By.XPATH, "//textarea[@name='descripcion']").send_keys("qwertyuXD")
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()
        time.sleep(10)

        # Validación de creación
        actual = "Se registro el producto de manera correcta"
        devuelto = driver.find_element(By.XPATH, "//div[@class='swal2-html-container']").text
        assert actual == devuelto, f"Error: Se esperaba '{actual}', pero se obtuvo '{devuelto}'"
        driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled']").click()
        time.sleep(3)

    def test_edit_product(self):
        driver = self.driver
        driver.find_element(By.XPATH, "(//i[@class='fas fa-pencil'])[1]").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//select[@class='form-control']//option[text()='Bebidas']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@class='form-control']").send_keys("")
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@name='precio_venta']").send_keys("")
        time.sleep(2)
        driver.find_element(By.XPATH, "//textarea[@name='descripcion']").send_keys("qwertyuXD")
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        time.sleep(3)

        # Validación de modificación
        actual = "Se actualizo el producto de manera correcta"
        devuelto = driver.find_element(By.XPATH, "//div[@class='swal2-html-container']").text
        assert actual == devuelto, f"Error: Se esperaba '{actual}', pero se obtuvo '{devuelto}'"
        driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled']").click()
        time.sleep(6)

    def test_view_another_product(self):
        driver = self.driver
        driver.find_element(By.XPATH, "(//a[@class='page-link'])[4]").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "(//i[@class='fas fa-eye'])[3]").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//a[@class='btn btn-secondary']").click()
        time.sleep(4)

    def test_view_product_list(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//select[@class='custom-select custom-select-sm form-control form-control-sm']//option[@value='10']").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//select[@class='custom-select custom-select-sm form-control form-control-sm']//option[@value='25']").click()
        time.sleep(5)

    def test_search_product(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//input[@class='form-control form-control-sm']").send_keys("agua")
        time.sleep(2)
        driver.find_element(By.XPATH, "(//i[@class='fas fa-eye'])[1]").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//a[@class='btn btn-secondary']").click()
        time.sleep(3)

    def test_delete_product(self):
        driver = self.driver
        driver.find_element(By.XPATH, "(//i[@class='fas fa-trash'])[1]").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled swal2-default-outline']").click()
        time.sleep(3)

        # Validación de eliminación
        actual = "Se eliminó el producto de manera correcta"
        devuelto = driver.find_element(By.XPATH, "//div[@class='swal2-html-container']").text
        assert actual == devuelto, f"Error: Se esperaba '{actual}', pero se obtuvo '{devuelto}'"
        driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled']").click()
        time.sleep(2)

    def test_complete(self):
        print("Prueba visual completada")
