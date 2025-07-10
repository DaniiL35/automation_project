from selenium.webdriver.common.by import By

complete_header = (By.CLASS_NAME, "complete-header")
complete_text = (By.CLASS_NAME, "complete-text")
finish_checkout_button = (By.ID, "back-to-products")


class CheckoutCompletePage:

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.find_element(complete_header[0], complete_header[1])

    def get_order_confirmation_message(self):
        return self.driver.find_element(complete_text[0], complete_text[1])

    def get_back_home_button(self):
        return self.driver.find_element(finish_checkout_button[0], finish_checkout_button[1])
