import pytest
import random
import allure
from utilities.common_ops import get_data
from workflows.web_flows import WebFlows

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
        WebFlows.checkout_proccess("test1", "test2", "1231")

    # upcoming tests
    # def test_logout(self):
    # def test_login_diffrent_user
    # def test_remove_product_from_cart

    # def teardown_method(self):
    # WebFlows.return_home()
