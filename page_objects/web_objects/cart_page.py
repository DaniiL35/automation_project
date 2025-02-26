from selenium.webdriver.common.by import By

continue_shopping_button = (By.ID, "continue-shopping")
checkout_button = (By.ID, "checkout")
cart_items = (By.CLASS_NAME, "cart_item")
remove_buttons = (By.XPATH, "//*[text()='Remove']")


class CartPage:

    def __init__(self, driver):
        self.driver = driver

    def get_continue_shopping_button(self):
        return self.driver.find_element(continue_shopping_button[0], continue_shopping_button[1])

    def get_checkout_button(self):
        return self.driver.find_element(checkout_button[0], checkout_button[1])

    def get_cart_items(self):
        return self.driver.find_elements(cart_items[0], cart_items[1])

    def get_remove_buttons(self):
        return self.driver.find_elements(remove_buttons[0], remove_buttons[1])

    
