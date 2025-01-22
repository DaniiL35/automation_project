from selenium.webdriver.common.by import By

cart_icon = (By.ID, "shopping_cart_container")
burger_menu = (By.ID, "react-burger-menu-btn")
all_items = (By.ID, "inventory_sidebar_link")
about = (By.ID, "about_sidebar_link")
logout = (By.ID), "logout_sidebar_link"
reset = (By.ID), "reset_sidebar_link"



class UppermenuPage:

    def __init__(self, driver):
        self.driver = driver

    def get_cart_icon(self):
        return self.driver.find_element(cart_icon[0], cart_icon[1])

    def get_burger_menu(self):
        return self.driver.find_element(burger_menu[0], burger_menu[1])

    def get_all_items(self):
        return self.driver.find_element(all_items[0], all_items[1])

    def get_about(self):
        return self.driver.find_element(about[0], about[1])

    def get_logout(self):
        return self.driver.find_element(logout[0], logout[1])

    def get_reset(self):
        return self.driver.find_element(reset[0], reset[1])
