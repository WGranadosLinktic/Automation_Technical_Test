class OpenStorePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://opencart.abstracta.us/index.php?route=common/home"
        # Maximizar la ventana del navegador
        self.driver.maximize_window()

    def open_page(self):
        # Abrir la página de la tienda
        self.driver.get(self.url)
