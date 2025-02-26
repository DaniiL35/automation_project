from selenium.webdriver.common.by import By

product_title = (By.XPATH, "//*[contains(@class, 'inventory_details_name') and contains(@class, 'large_size')]")
product_description = (By.XPATH, "//*[contains(@class, 'inventory_details_desc') and contains(@class, 'large_size')]")
product_price = (By.CLASS_NAME, "inventory_details_price")
buy_button = (By.XPATH, "//*[contains(@class, 'btn') and contains(@class, 'btn_primary') and contains(@class, 'btn_small') and contains(@class, 'btn_inventory')]")
back_to_products = (By.ID, "back-to-products")


class ProductPage:

    def __init__(self, driver):
        self.driver = driver

    def get_product_title(self):
        return self.driver.find_element(product_title[0], product_title[1])

    def get_product_description(self):
        return self.driver.find_element(product_description[0], product_description[1])

    def get_product_price(self):
        return self.driver.find_element(product_price[0], product_price[1])

    def get_buy_button(self):
        return self.driver.find_element(buy_button[0], buy_button[1])

    def get_back_to_products(self):
        return self.driver.find_element(back_to_products[0], back_to_products[1])
