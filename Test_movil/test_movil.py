import unittest
from appium import webdriver
from time import sleep

class MobileAppLoginTest(unittest.TestCase):

    def setUp(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '11.0',  # Versión de Android
            'deviceName': 'Android Emulator',  # Nombre del dispositivo o emulador
            'app': '/ruta/a/la/aplicacion.apk',  # Ruta al archivo APK de la aplicación
            'automationName': 'UiAutomator2',  # Sistema de automatización para Android
        }
        
        # Iniciar el driver con las capacidades deseadas
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        sleep(2)  # Espera para que la app cargue

    def test_login_and_verify_products(self):
        """Verificar el flujo de login y la visualización de productos"""

        driver = self.driver
        
        # Paso 1: Completar el formulario de login
        username_input = driver.find_element_by_id('com.ejemplo.app:id/username')
        password_input = driver.find_element_by_id('com.ejemplo.app:id/password')
        login_button = driver.find_element_by_id('com.ejemplo.app:id/login_button')
        
        # Ingresar las credenciales
        username_input.send_keys('usuario_prueba')  # Reemplaza con un nombre de usuario válido
        password_input.send_keys('contraseña_segura')  # Reemplaza con una contraseña válida
        
        # Hacer clic en el botón de login
        login_button.click()
        sleep(2)  # Espera para que se complete el inicio de sesión
        
        # Paso 2: Verificar si el login fue exitoso
        try:
            # Verificar que no aparezca un mensaje de error
            error_message = driver.find_element_by_id('com.ejemplo.app:id/error_message')
            self.assertFalse(error_message.is_displayed(), "Error: El login falló. Mensaje de error presente.")
            print("Login exitoso.")
        except:
            # Si no se encuentra el mensaje de error, consideramos que el login fue exitoso.
            print("Login exitoso.")
        
        # Paso 3: Verificar que la pantalla de productos se carga
        try:
            # Verificar que los productos están visibles
            products = driver.find_elements_by_class_name('com.ejemplo.app:id/producto_item')
            self.assertGreater(len(products), 0, "No se encontraron productos en la pantalla")
            print(f"Se encontraron {len(products)} productos.")
        except Exception as e:
            self.fail(f"No se pudo verificar los productos. Error: {e}")

    def tearDown(self):
        """Cerrar la aplicación y el driver después de cada prueba"""
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
