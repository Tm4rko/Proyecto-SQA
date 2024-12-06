from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestProductos:
    
   
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

    def test_navigate_to_products(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//i[@class='fas fa-fw fa-list ']//following-sibling::p[contains(text(), 'Productos')]").click()
        time.sleep(2)
        
        driver.find_element(By.XPATH, "//i[@class='far fa-fw fa-circle ']//following-sibling::p[contains(text(), 'Productos')]").click()
        time.sleep(2)

       
        actual = "Listado de Productos"  
        devuelto = driver.find_element(By.XPATH,"//i[@class='far fa-fw fa-circle ']//following-sibling::p[contains(text(), 'Listado de Productos')]").text  
        assert actual in devuelto, f"Error en la visualización de la categoria: Se esperaba '{actual}', pero se obtuvo '{devuelto}'"
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
        ruta_logo = "C:\\xampp\htdocs\\Proyecto-SQA\\Proyecto-SQA\\pepsi.jpg"
        driver.find_element(By.XPATH, "//input[@name='imagen']").send_keys(ruta_logo)


        time.sleep(2)
        driver.find_element(By.XPATH, "//textarea[@name='descripcion']").send_keys("qwertyuXD")
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()
        time.sleep(2)

        actual = "Se registro el producto de manera correcta"
        devuelto = driver.find_element(By.XPATH, "//div[@class='swal2-html-container']").text
        assert actual == devuelto, f"Error: Se esperaba '{actual}', pero se obtuvo '{devuelto}'"
        driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled']").click()
        time.sleep(3)

    def test_edit_product(self):
        driver = self.driver
        driver.find_element(By.XPATH, "(//i[@class='fas fa-pencil'])[1]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//select[@class='form-control']//option[text()='Bebidas']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@class='form-control']").send_keys("")
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@name='precio_venta']").send_keys("")
        time.sleep(2)
        ruta_logo = "C:\\xampp\\htdocs\\Proyecto-SQA\\Proyecto-SQA\\agua.png"
        driver.find_element(By.XPATH, "//input[@name='imagen']").send_keys(ruta_logo)
        time.sleep(2)
        driver.find_element(By.XPATH, "//textarea[@name='descripcion']").send_keys("qwertyuXD")
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        time.sleep(2)

        actual = "Se actualizo el producto de manera correcta"
        devuelto = driver.find_element(By.XPATH, "//div[@class='swal2-html-container']").text
        assert actual == devuelto, f"Error: Se esperaba '{actual}', pero se obtuvo '{devuelto}'"
        driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled']").click()
        time.sleep(2)

    def test_view_another_product(self):
        driver = self.driver
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[@data-dt-idx='2']").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//a[contains(@href,'115')]//i[@class='fas fa-eye']").click()
        time.sleep(3)

        actual = "Punta de S"  
        devuelto = driver.find_element(By.XPATH,"(//div[@class='form-group'])[2]").text  
        assert actual in devuelto, f"Error en la visualización de la categoria: Se esperaba '{actual}', pero se obtuvo '{devuelto}'"  

        driver.find_element(By.XPATH, "//a[@class='btn btn-secondary']").click()
        time.sleep(2)



    def test_view_another_product_original(self):
        driver = self.driver
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        driver.find_element(By.XPATH, "(//i[@class='fas fa-eye'])[1]").click()
        time.sleep(3)

        actual = "agua vital"  
        devuelto = driver.find_element(By.XPATH,"(//div[@class='form-group'])[2]").text  
        assert actual in devuelto, f"Error en la visualización de la categoria: Se esperaba '{actual}', pero se obtuvo '{devuelto}'"  

        driver.find_element(By.XPATH, "//a[@class='btn btn-secondary']").click()
        time.sleep(2)



    def test_view_product_list(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//select[@class='custom-select custom-select-sm form-control form-control-sm']//option[@value='10']").click()
        time.sleep(2)

        
        driver.find_element(By.XPATH, "//select[@class='custom-select custom-select-sm form-control form-control-sm']//option[@value='25']").click()
        time.sleep(2)

        actual = "25"  
        devuelto = driver.find_element(By.XPATH,"//select[@class='custom-select custom-select-sm form-control form-control-sm']").text  
        assert actual in devuelto, f"Error en la visualización de la categoria: Se esperaba '{actual}', pero se obtuvo '{devuelto}'"
        time.sleep(2)


    def test_search_product(self):
        driver = self.driver
        driver.find_element(By.XPATH, "//input[@class='form-control form-control-sm']").send_keys("agua vital")
        time.sleep(2)

        actual = "agua vital"  
        devuelto = driver.find_element(By.XPATH,"(//td[@style='vertical-align: middle;'])[2]").text  
        assert actual in devuelto, f"Error en la visualización de la categoria: Se esperaba '{actual}', pero se obtuvo '{devuelto}'"
        time.sleep(2)

    def test_view_another_product_original(self):
        driver = self.driver
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        driver.find_element(By.XPATH, "(//i[@class='fas fa-eye'])[1]").click()
        time.sleep(3)

        actual = "agua vital"  
        devuelto = driver.find_element(By.XPATH,"(//div[@class='form-group'])[2]").text  
        assert actual in devuelto, f"Error en la visualización de la categoria: Se esperaba '{actual}', pero se obtuvo '{devuelto}'"  

        driver.find_element(By.XPATH, "//a[@class='btn btn-secondary']").click()
        time.sleep(2)

        

    def test_delete_product(self):
        driver = self.driver
        driver.find_element(By.XPATH, "(//i[@class='fas fa-trash'])[1]").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled swal2-default-outline']").click()
        time.sleep(2)

        actual = "Se eliminó el producto de manera correcta"
        devuelto = driver.find_element(By.XPATH, "//div[@class='swal2-html-container']").text
        assert actual == devuelto, f"Error: Se esperaba '{actual}', pero se obtuvo '{devuelto}'"
        driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled']").click()
        time.sleep(2)

    def test_complete(self):
        print("Prueba visual completada")

    def teardown_class(self):
        self.driver.quit()
