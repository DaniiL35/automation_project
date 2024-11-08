from selenium.webdriver.common.by import By

username = (By.NAME, 'user-name')
password = (By.NAME, 'password')
login_button = (By.ID, 'login-button')


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def get_username(self):
        return self.driver.find_element(username[0], username[1])

    def get_password(self):
        return self.driver.find_element(password[0], password[1])

    def get_login_button(self):
        return self.driver.find_element(login_button[0], login_button[1])

