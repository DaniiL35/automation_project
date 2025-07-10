import test_cases.conftest
from page_objects.web_objects.checkout_complete_page import CheckoutCompletePage
from page_objects.web_objects.inventory_page import InventoryPage
from page_objects.web_objects.login_page import LoginPage
from page_objects.web_objects.upper_menu_page import UppermenuPage
from page_objects.web_objects.product_page import ProductPage
from page_objects.web_objects.cart_page import CartPage
from page_objects.web_objects.checkout_page import CheckoutPage
from page_objects.web_objects.overview_page import OverviewPage

# web objects
web_login = None
web_inventory = None
web_upper_menu = None
product_page = None
cart_page = None
checkout_page = None
overview_page = None
checkout_complete_page = None


class ManagePages:

    @staticmethod
    def init_web_pages():
        globals()['web_login'] = LoginPage(test_cases.conftest.driver)
        globals()['web_inventory'] = InventoryPage(test_cases.conftest.driver)
        globals()['web_upper_menu'] = UppermenuPage(test_cases.conftest.driver)
        globals()['product_page'] = ProductPage(test_cases.conftest.driver)
        globals()['cart_page'] = CartPage(test_cases.conftest.driver)
        globals()['checkout_page'] = CheckoutPage(test_cases.conftest.driver)
        globals()['overview_page'] = OverviewPage(test_cases.conftest.driver)
        globals()['checkout_complete_page'] = CheckoutCompletePage(test_cases.conftest.driver)
