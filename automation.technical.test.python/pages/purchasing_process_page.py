import openpyxl
import configparser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from elements.purchasing_process_elements import PurchasingElements

class PurchasingPage:
    def __init__(self, driver):
        self.driver = driver
        self.elements = PurchasingElements()
        self.load_property()  # Cargar configuraciones desde el archivo .ini

    def load_property(self):
        """ Cargar configuraciones desde el archivo .ini """
        config = configparser.ConfigParser()
        config.read('yourstore.ini')  # Ruta al archivo .ini
        # Cargar configuraciones de la compra
        self.loadProperty = {
            "tituloCheckout": config.get("General", "tituloCheckout", fallback="Checkout - Your Store")
        }

    def select_product(self):
        """ Selecciona el producto de la tienda """
        self.driver.find_element(*self.elements.BTN_PHONE).click()
        assert self.driver.title == "Phones & PDAs", f"Se esperaba el título 'Phones & PDAs', pero obtuvo {self.driver.title}"
        print("La página de la categoría seleccionada se abrió correctamente.")
    
    def add_product_to_cart(self):
        """ Agrega el producto al carrito """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.elements.PRODUCT_PHONE)
        )
        self.driver.find_element(*self.elements.PRODUCT_PHONE).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.elements.BTN_ADD_CART)
        )
        self.driver.find_element(*self.elements.BTN_ADD_CART).click()
        print("Producto agregado al carrito correctamente.")

    def view_cart(self):
        """ Ingresa al carrito de compras """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.elements.BTN_ITEMS_CART)
        )
        self.driver.find_element(*self.elements.BTN_ITEMS_CART).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.elements.BTN_VIEW_CART)
        )
        self.driver.find_element(*self.elements.BTN_VIEW_CART).click()
        assert self.driver.title == "Shopping Cart", f"Se esperaba el título 'Shopping Cart', pero obtuvo {self.driver.title}"
        print("La página del carrito de compras se abrió correctamente.")

    def start_checkout_process(self):
        """ Inicia el proceso de pago """
        self.driver.find_element(*self.elements.BTN_CHECKOUT).click()
        assert self.driver.title == self.loadProperty["tituloCheckout"], f"Se esperaba el título '{self.loadProperty['tituloCheckout']}', pero obtuvo {self.driver.title}"
        print("La página de checkout se abrió correctamente.")

    def enter_customer_details(self, first_name, last_name, email, phone, company, address1, address2, city, postcode):
        """ Diligencia los datos del cliente """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.elements.CHECK_GUEST_CHECKOUT)
        )
        self.driver.find_element(*self.elements.CHECK_GUEST_CHECKOUT).click()
        self.driver.find_element(*self.elements.BTN_CONTINUE_CHECKOUT).click()
        
        self.driver.find_element(*self.elements.TXT_FIRST_NAME).send_keys(first_name)
        self.driver.find_element(*self.elements.TXT_LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.elements.TXT_EMAIL).send_keys(email)
        self.driver.find_element(*self.elements.TXT_TELEPHONE).send_keys(phone)
        self.driver.find_element(*self.elements.TXT_COMPANY).send_keys(company)
        self.driver.find_element(*self.elements.TXT_ADDRESS1).send_keys(address1)
        self.driver.find_element(*self.elements.TXT_ADDRESS2).send_keys(address2)
        self.driver.find_element(*self.elements.TXT_CITY).send_keys(city)
        self.driver.find_element(*self.elements.TXT_POST_CODE).send_keys(postcode)
        
        self.driver.find_element(*self.elements.LST_COUNTRY_COLOMBIA).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.elements.LST_REGION_STATE_BOGOTA)
        )
        self.driver.find_element(*self.elements.LST_REGION_STATE).click()
        self.driver.find_element(*self.elements.LST_REGION_STATE_BOGOTA).click()
        
        self.driver.find_element(*self.elements.BTN_CONTINUE_CUSTOMER_DATA).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.elements.BTN_CONTINUE_DELIVERY_METHOD)
        )
        self.driver.find_element(*self.elements.BTN_CONTINUE_DELIVERY_METHOD).click()

    def select_payment_method(self):
        """ Selecciona el método de pago """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.elements.CHECK_PAYMENT_METHOD)
        )
        self.driver.find_element(*self.elements.CHECK_PAYMENT_METHOD).click()
        self.driver.find_element(*self.elements.BTN_CONTINUE_PAYMENT_METHOD).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.elements.BTN_CONFIRM_ORDER)
        )
        print("Método de pago seleccionado correctamente.")

    def confirm_purchase(self):
        """ Confirma la compra """
        self.driver.find_element(*self.elements.BTN_CONFIRM_ORDER).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.elements.BTN_CONTINUE_ORDER_OK)
        )
        assert "Your order has been placed!" in self.driver.page_source, "La orden no se ha confirmado correctamente."
        print("La compra ha sido confirmada correctamente.")