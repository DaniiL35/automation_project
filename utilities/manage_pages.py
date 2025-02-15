import test_cases.conftest
from page_objects.web_objects.inventory_page import InventoryPage
from page_objects.web_objects.login_page import LoginPage
from page_objects.web_objects.upper_menu_page import UppermenuPage

# web objects
web_login = None
web_inventory = None
web_upper_menu = None


class ManagePages:
    @staticmethod
    def init_web_pages():
        globals()['web_login'] = LoginPage(test_cases.conftest.driver)
        globals()['web_inventory'] = InventoryPage(test_cases.conftest.driver)
        globals()['web_upper_menu'] = UppermenuPage(test_cases.conftest.driver)

