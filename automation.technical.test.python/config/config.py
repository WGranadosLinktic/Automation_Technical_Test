import os

# Nombre del proyecto (puede ser útil como constante)
PROJECT_NAME = "automation.technical.test.python"

# Configuración del WebDriver
WEBDRIVER_DRIVER = "chrome"  # En este caso, solo chrome está configurado
CHROME_DRIVER_PATH = os.path.join(os.getcwd(), "drivers", "chromedriver.exe")

# Verifica la ruta generada para chromedriver
print(f"Ruta de chromedriver: {CHROME_DRIVER_PATH}")

# URL base para las pruebas
BASE_URL = "https://opencart.abstracta.us/index.php?route=common/home"

# Timeout de espera
TIMEOUT = 5  # Timeout general en segundos
IMPLICIT_WAIT = 5  # Tiempo de espera implícito para encontrar elementos
PAGE_LOAD_TIMEOUT = 5  # Timeout para cargar la página

# Configuración de maximizar el navegador
BROWSER_MAXIMIZED = True

# Otros parámetros si los necesitas (por ejemplo, control de logs, etc.)
SHOW_STEP_DETAILS = True