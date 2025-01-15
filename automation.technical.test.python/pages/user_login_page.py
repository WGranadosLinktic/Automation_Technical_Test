from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from elements.open_store_elements import OpenStoreElements  # Importar los elementos
from elements.user_login_elements import UserLoginElements  # Importar los elementos
import configparser

class UserLoginPage:
    def __init__(self, driver):
        self.driver = driver
        # Cargar configuraciones desde el archivo .ini
        self.load_property()

    def load_property(self):
        # Leer el archivo .ini
        config = configparser.ConfigParser()
        config.read('yourstore.ini')  # Ruta al archivo .ini

        # Cargar configuraciones
        self.loadProperty = {
            "tituloLogin": config.get("General", "tituloLogin", fallback="Account Login"),
            "lbl_LoginOK": config.get("General", "lbl_LoginOK", fallback="My Account")
        }

    def open_user_login(self):
        # Aquí no esperamos ni accedemos a self.url, ya que la página ya fue abierta por OpenStorePage
        # Esperar a que el botón "My Account" sea visible y luego hacer clic para abrir login
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, OpenStoreElements.BTN_MY_ACCOUNT))
        )
        my_account_button = self.driver.find_element(By.XPATH, OpenStoreElements.BTN_MY_ACCOUNT)

        # Mover a la posición del botón y hacer clic
        actions = ActionChains(self.driver)
        actions.move_to_element(my_account_button).perform()
        my_account_button.click()

        # Esperar a que el botón de login sea visible
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, UserLoginElements.BTN_LOGIN))
        )

        # Hacer clic en el botón de login
        login_button = self.driver.find_element(By.XPATH, UserLoginElements.BTN_LOGIN)
        login_button.click()

        # Esperar a que la página de login esté completamente cargada
        WebDriverWait(self.driver, 10).until(
            EC.title_is(self.loadProperty["tituloLogin"])
        )

        # Verificar que el título de la página sea el esperado
        current_title = self.driver.title
        print(f"Título actual de la página: {current_title}")
        assert current_title == self.loadProperty["tituloLogin"], f"El título de la página no es correcto. Se esperaba '{self.loadProperty['tituloLogin']}' y se obtuvo '{current_title}'"

        print("El módulo de login de usuario se abrió correctamente")

    def enter_email(self, email):
        print(f"email: {email}")
        xpathEmail = (UserLoginElements.TXT_EMAIL)
        print(f"xpathEmail: {xpathEmail}")
        email_field = self.driver.find_element(By.XPATH, UserLoginElements.TXT_EMAIL)
        email_field.clear()
        email_field.send_keys(email)
        print(f"Se diligenció el campo Email: {email}")

    def enter_password(self, password):
        password_field = self.driver.find_element(By.XPATH, UserLoginElements.TXT_PASSWORD)
        password_field.clear()
        password_field.send_keys(password)
        print(f"Se diligenció el campo Password")

    def confirm_login(self):
        # Hacer clic en el botón de login para confirmar
        login_button = self.driver.find_element(By.XPATH, UserLoginElements.BTN_LOGIN_CONFIRM)
        login_button.click()

        # Esperar la confirmación de login
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, UserLoginElements.MSG_LOGIN_OK))
        )

        # Verificar el mensaje de login exitoso
        login_success_message = self.driver.find_element(By.XPATH, UserLoginElements.MSG_LOGIN_OK)
        texto_extraido = login_success_message.text
        print(f"texto_extraido: {texto_extraido}")
        texto_esperado = self.loadProperty["lbl_LoginOK"]
        print(f"texto_esperado: {texto_esperado}")
        assert texto_extraido == texto_esperado
        print("El login de usuario se realizó de forma exitosa")
