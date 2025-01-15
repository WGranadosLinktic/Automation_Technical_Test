from selenium.webdriver.common.by import By

class UserRegisterElements:
    BTN_REGISTER = ("/html/body/nav/div/div[2]/ul/li[2]/ul/li[1]/a")
    TXT_FIRST_NAME = ("/html/body/div[2]/div/div/form/fieldset[1]/div[2]/div/input")
    TXT_LAST_NAME = ("/html/body/div[2]/div/div/form/fieldset[1]/div[3]/div/input")
    TXT_EMAIL = ("/html/body/div[2]/div/div/form/fieldset[1]/div[4]/div/input")
    TXT_TELEPHONE = ("/html/body/div[2]/div/div/form/fieldset[1]/div[5]/div/input")
    TXT_PASSWORD = ("/html/body/div[2]/div/div/form/fieldset[2]/div[1]/div/input")
    TXT_CONFIRM_PASSWORD = ("/html/body/div[2]/div/div/form/fieldset[2]/div[2]/div/input")
    CHECK_PRIVACY_POLICY = ("/html/body/div[2]/div/div/form/div/div/input[1]")
    BTN_CONTINUE = ("/html/body/div[2]/div/div/form/div/div/input[2]")
    MSG_REGISTER_OK = ("/html/body/div[2]/div/div/p[1]")