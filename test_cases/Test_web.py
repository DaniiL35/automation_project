import pytest
import random
import allure
from utilities.common_ops import get_data
from workflows.web_flows import WebFlows
import test_cases.conftest as conf

r_ID = random.randint(0, 5)


@pytest.mark.usefixtures('init_web_driver')
class Test_web:
    @allure.title('Test01: Verify Login to "Swag Labs"')
    @allure.description('This test verifies the login functionality of the "Swag Labs" website.')
    def test_verify_login(self):
        WebFlows.login_flow(get_data('Username'), get_data('Password'))
        WebFlows.verify_title("Products")

    @allure.title('Test02: Verify Menu Buttons')
    @allure.description('This test verifies the functionality of the menu buttons in the "Swag Labs" website.')
    def test_verify_menu_buttons(self):
        WebFlows.verify_menu_buttons_flow()

    @allure.title('Test03: Verify Products')
    @allure.description('This test verifies the details of products in the main page .')
    def test_verify_products(self):
        WebFlows.verifiy_products_names_and_desc()

    @allure.title('Test04: Verify Product Page')
    @allure.description('This test verifies the details of the product on the product page in the "Swag Labs" website.')
    def test_verify_product_page(self):
        WebFlows.verify_product_page_details()

    @allure.title('Test05: Add Product to Cart')
    @allure.description('This test adds a product to the cart and verifies it in the "Swag Labs" website.')
    def test_cart(self):
        WebFlows.add_and_verifiy_product_in_cart(r_ID)

    @allure.title('Test06: Checkout Process')
    @allure.description('This test verifies the checkout process in the "Swag Labs" website.')
    def test_checkout(self):
        WebFlows.checkout_proccess(get_data("firstname"), get_data("lastname"), get_data('postalcode'))
        WebFlows.verify_checkout_complete_page()

    @allure.title('Test07: remove product from cart')
    @allure.description('This test verifies the removal of a product from the cart in the "Swag Labs" website.')
    def test_remove_product_from_cart(self):
        WebFlows.add_product_to_cart(r_ID)
        WebFlows.remove_product_from_cart(get_data("last_product_index"))
        WebFlows.verify_cart_is_empty()

    @allure.title('Test08: logout')
    @allure.description('This test verifies the logout functionality in the "Swag Labs" website.')
    def test_logout(self):
        WebFlows.logout_flow()

    @allure.title('TestTBA: visual testing')
    @allure.description('This test is for visual testing of the "Swag Labs" website.')
    @pytest.mark.skipif(get_data('Execute_Applitools').lower() == 'no', reason="Visual testing is disabled")
    def test_broken_user(self):
        conf.eyes.open(self.driver, "Swag Labs", "Broken User Test", )
        WebFlows.login_flow(get_data('Username_broken'), get_data('Password'))
        conf.eyes.check_window("Broken User")

    # def teardown_method(self):
    # WebFlows.return_home()
