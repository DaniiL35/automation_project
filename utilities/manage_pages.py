import test_cases.conftest as conf
from page_objects.web_objects.checkout_complete_page import CheckoutCompletePage
from page_objects.web_objects.inventory_page import InventoryPage
from page_objects.web_objects.login_page import LoginPage
from page_objects.web_objects.upper_menu_page import UppermenuPage
from page_objects.web_objects.product_page import ProductPage
from page_objects.web_objects.cart_page import CartPage
from page_objects.web_objects.checkout_page import CheckoutPage
from page_objects.web_objects.overview_page import OverviewPage
from page_objects.mobile_objects.calculator_page import CalculatorPage
from page_objects.mobile_objects.saved_page import SavedPage

# web objects
web_login = None
web_inventory = None
web_upper_menu = None
product_page = None
cart_page = None
checkout_page = None
overview_page = None
checkout_complete_page = None

# mobile objects
mobile_calculator = None
mobile_saved = None


class ManagePages:

    @staticmethod
    def init_web_pages():
        globals()['web_login'] = LoginPage(conf.driver)
        globals()['web_inventory'] = InventoryPage(conf.driver)
        globals()['web_upper_menu'] = UppermenuPage(conf.driver)
        globals()['product_page'] = ProductPage(conf.driver)
        globals()['cart_page'] = CartPage(conf.driver)
        globals()['checkout_page'] = CheckoutPage(conf.driver)
        globals()['overview_page'] = OverviewPage(conf.driver)
        globals()['checkout_complete_page'] = CheckoutCompletePage(conf.driver)

    @staticmethod
    def init_mobile_pages():
        globals()['mobile_calculator'] = CalculatorPage(conf.driver)
        globals()['mobile_saved'] = SavedPage(conf.driver)
