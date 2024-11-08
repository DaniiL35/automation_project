from selenium.webdriver.common.by import By




class InventoryPage:
    def __init__(self, driver):
        self.driver = driver


    def verify_page(self):
        return self.driver.find_element(by.NAME, 'title')