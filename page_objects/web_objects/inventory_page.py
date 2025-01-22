from selenium.webdriver.common.by import By

title = (By.CLASS_NAME, "title")


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def get_main_title(self):
        return self.driver.find_element(title[0], title[1])
