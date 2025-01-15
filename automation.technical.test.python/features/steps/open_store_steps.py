from behave import given
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Paso definido para el feature
@given('El usuario ingresa a la página de Your Store')
def step_impl(context):
    # Usa el contexto que fue configurado en environment.py
    context.open_store_page.open_page()