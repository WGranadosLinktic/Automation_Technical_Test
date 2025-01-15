#Author: william.granados@linktic.com
@YourStore
Feature: Validar sitio ecommerce Your Store

	Background:
		Given El usuario ingresa a la página de Your Store

  @user_Register
  Scenario: Validar el registro de usuario
    When El usuario ingresa al módulo de registro de usuario
    And Ingresa el nombre desde el archivo userRegister.xlsx fila "1"
    And Ingresa el apellido desde el archivo userRegister.xlsx fila "1"
    And Ingresa el correo electronico desde el archivo userRegister.xlsx fila "1"
    And Ingresa el telefono desde el archivo userRegister.xlsx fila "1"
    And Ingresa la contraseña desde el archivo userRegister.xlsx fila "1"
    And Ingresa nuevamente la contraseña desde el archivo userRegister.xlsx fila "1"
    Then Confirmar creación de usuario
    
  @user_Login
  Scenario: Validar el login de usuario
    When El usuario ingresa al módulo de logueo de usuario
    And Ingresa el correo electronico desde el archivo userLogin.xlsx fila "1"
    And Ingresa la contraseña desde el archivo userLogin.xlsx fila "1"
    Then Confirmar login de usuario
    
  @selectProduct_addCart_buy
  Scenario: Realizar flujo de compra
    When El usuario selecciona un producto de la tienda
    And Agrega el producto al carrito de compras
    And Ingresa al carrito de compras
    And Inicia proceso de pago
    And Diligencia los datos del cliente desde el archivo customerData.xlsx fila "1"
    And Selecciona el metodo de pago
    Then Confirma compra