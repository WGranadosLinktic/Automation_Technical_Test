from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from elements.open_store_elements import OpenStoreElements  # Importar los elementos
from elements.user_register_elements import UserRegisterElements  # Importar los elementos
import configparser

# Importar OpenStorePage
from pages.open_store_page import OpenStorePage  # Esta es la línea que falta

class UserRegisterPage:
    def __init__(self, driver):
        self.driver = driver
        # Usamos OpenStorePage para abrir la tienda (sin definir la URL aquí)
        self.store_page = OpenStorePage(driver)
        self.store_page.open_page()  # Llamamos al método de OpenStorePage para abrir la página
        
        # Cargar configuraciones desde el archivo .ini
        self.load_property()

    def load_property(self):
        # Leer el archivo .ini
        config = configparser.ConfigParser()
        config.read('yourstore.ini')  # Ruta al archivo .ini

        # Cargar configuraciones
        self.loadProperty = {
            "tituloRegister": config.get("PageSettings", "tituloRegister", fallback="Register Account"),
            "msg_RegisterOK": config.get("PageSettings", "msg_RegisterOK", fallback="Congratulations! Your new account has been successfully created!")
        }

    def open_user_register(self):
        # Aquí no esperamos ni accedemos a self.url, ya que la página ya fue abierta por OpenStorePage

        # Esperar a que el botón "My Account" sea visible y luego hacer clic
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, OpenStoreElements.BTN_MY_ACCOUNT))
        )
        my_account_button = self.driver.find_element(By.XPATH, OpenStoreElements.BTN_MY_ACCOUNT)

        # Mover a la posición del botón y hacer clic
        actions = ActionChains(self.driver)
        actions.move_to_element(my_account_button).perform()
        my_account_button.click()

        # Esperar a que el botón de registro sea visible
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, UserRegisterElements.BTN_REGISTER))
        )

        # Hacer clic en el botón de registro
        register_button = self.driver.find_element(By.XPATH, UserRegisterElements.BTN_REGISTER)
        register_button.click()

        # Verificar que la página de registro cargue correctamente
        assert self.driver.title == self.loadProperty["tituloRegister"]
        print("El módulo de registro de usuario se abrió correctamente")

    def enter_first_name(self, firstname):
        first_name_field = self.driver.find_element(By.XPATH, UserRegisterElements.TXT_FIRST_NAME)
        first_name_field.clear()
        first_name_field.send_keys(firstname)
        print(f"Se diligenció el campo First Name: {firstname}")

    def enter_last_name(self, lastname):
        last_name_field = self.driver.find_element(By.XPATH, UserRegisterElements.TXT_LAST_NAME)
        last_name_field.clear()
        last_name_field.send_keys(lastname)
        print(f"Se diligenció el campo Last Name: {lastname}")

    def enter_email(self, email):
        email_field = self.driver.find_element(By.XPATH, UserRegisterElements.TXT_EMAIL)
        email_field.clear()
        email_field.send_keys(email)
        print(f"Se diligenció el campo Email: {email}")

    def enter_telephone(self, telephone):
        telephone_field = self.driver.find_element(By.XPATH, UserRegisterElements.TXT_TELEPHONE)
        telephone_field.clear()
        telephone_field.send_keys(telephone)
        print(f"Se diligenció el campo Telephone: {telephone}")

    def enter_password(self, password):
        password_field = self.driver.find_element(By.XPATH, UserRegisterElements.TXT_PASSWORD)
        password_field.clear()
        password_field.send_keys(password)
        print(f"Se diligenció el campo Password")

    def enter_confirm_password(self, confirmpassword):
        confirm_password_field = self.driver.find_element(By.XPATH, UserRegisterElements.TXT_CONFIRM_PASSWORD)
        confirm_password_field.clear()
        confirm_password_field.send_keys(confirmpassword)
        print(f"Se diligenció el campo Confirm Password")

    def confirm_register(self):
        # Marcar la política de privacidad
        privacy_policy_checkbox = self.driver.find_element(By.XPATH, UserRegisterElements.CHECK_PRIVACY_POLICY)
        privacy_policy_checkbox.click()

        # Hacer clic en continuar
        continue_button = self.driver.find_element(By.XPATH, UserRegisterElements.BTN_CONTINUE)
        continue_button.click()

        # Esperar la confirmación de registro
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, UserRegisterElements.MSG_REGISTER_OK))
        )

        # Verificar el mensaje de registro exitoso
        register_success_message = self.driver.find_element(By.XPATH, UserRegisterElements.MSG_REGISTER_OK)
        texto_extraido = register_success_message.text
        print(f"texto_extraido: {texto_extraido}")
        texto_esperado = self.loadProperty["msg_RegisterOK"]
        print(f"texto_esperado: {texto_esperado}")
        assert texto_extraido == texto_esperado
        #assert register_success_message.text == self.loadProperty["msg_RegisterOK"]
        print("El registro de usuario se realizó de forma exitosa")