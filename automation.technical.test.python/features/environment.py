from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.open_store_page import OpenStorePage  # Asegúrate de importar la clase de la página
from config.config import CHROME_DRIVER_PATH, IMPLICIT_WAIT
from features.steps.user_register_steps import UserRegisterSteps
from features.steps.user_login_steps import UserLoginSteps
from features.steps.purchasing_process_steps import PurchasingProcessSteps

# Este método se ejecutará antes de que inicien las pruebas
def before_all(context):
    print("Iniciando el contexto y el driver")
    # Crear un servicio para el WebDriver
    service = Service(CHROME_DRIVER_PATH)
    context.driver = webdriver.Chrome(service=service)
    context.driver.implicitly_wait(IMPLICIT_WAIT)
    # Instanciar la página principal
    context.open_store_page = OpenStorePage(context.driver)
    # Inicializar UserRegisterSteps
    context.user_register_steps = UserRegisterSteps()
    # Inicializar UserRegisterSteps
    context.user_login_steps = UserLoginSteps()
    # Inicializar PurchasingProcessSteps
    context.purchasing_process_steps = PurchasingProcessSteps()

# Este método se ejecutará después de que terminen todas las pruebas
def after_all(context):
    context.driver.quit()
