from selenium.webdriver.common.by import By

title = (By.CLASS_NAME, "title")
products_names = (By.CLASS_NAME, "inventory_item_name")
products_description = (By.CLASS_NAME, "inventory_item_desc")
prices = (By.CLASS_NAME, "inventory_item_price")

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def get_main_title(self):
        return self.driver.find_element(title[0], title[1])

    def get_products(self):
        return self.driver.find_elements(products_names[0], products_names[1])

    def get_products_description(self):
        return self.driver.find_elements(products_description[0], products_description[1])

    def get_product_description(self, index):
        return self.get_products_description()[index]

    def get_prices(self):
        return self.driver.find_elements(prices[0], prices[1])



