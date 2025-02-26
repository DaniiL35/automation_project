from selenium.webdriver.common.by import By

price_total = (By.CLASS_NAME, "summary_total_label")
finish_button = (By.ID, "finish")
cancel_button = (By.ID, "cancel")
items = (By.CLASS_NAME, "cart_item_label")


class OverviewPage:

    def __init__(self, driver):
        self.driver = driver

    def get_price_total(self):
        return self.driver.find_element(price_total[0], price_total[1])

    def get_finish_button(self):
        return self.driver.find_element(finish_button[0], finish_button[1])

    def get_cancel_button(self):
        return self.driver.find_element(cancel_button[0], cancel_button[1])

    def get_items(self):
        return self.driver.find_elements(items[0], items[1])
