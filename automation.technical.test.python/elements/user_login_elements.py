from selenium.webdriver.common.by import By

class UserLoginElements:
    BTN_MY_ACCOUNT = ("//li[@class='dropdown']/a/span[1][@class='hidden-xs hidden-sm hidden-md']")
    BTN_LOGIN = ("/html/body/nav/div/div[2]/ul/li[2]/ul/li[2]/a")
    TXT_EMAIL = ("/html/body/div[2]/div/div/div/div[2]/div/form/div[1]/input")
    TXT_PASSWORD = ("/html/body/div[2]/div/div/div/div[2]/div/form/div[2]/input")
    BTN_LOGIN_CONFIRM = ("/html/body/div[2]/div/div/div/div[2]/div/form/input")
    MSG_LOGIN_OK = ("/html/body/div[2]/div/div/h2[1]")