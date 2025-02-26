from selenium.webdriver.common.by import By

first_name_field = (By.ID, "first-name")
last_name_field = (By.ID, "last-name")
postal_code_field = (By.ID, "postal-code")
continue_button = (By.ID, "continue")
cancel_button = (By.ID, "cancel")


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    def get_first_name_field(self):
        return self.driver.find_element(first_name_field[0], first_name_field[1])

    def get_last_name_field(self):
        return self.driver.find_element(last_name_field[0], last_name_field[1])

    def get_postal_code_field(self):
        return self.driver.find_element(postal_code_field[0], postal_code_field[1])

    def get_continue_button(self):
        return self.driver.find_element(continue_button[0], continue_button[1])

    def get_cancel_button(self):
        return self.driver.find_element(cancel_button[0], cancel_button[1])
