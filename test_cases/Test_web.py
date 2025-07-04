import pytest
import random
from utilities.common_ops import get_data
from workflows.web_flows import WebFlows

r_ID = random.randint(0,5)


@pytest.mark.usefixtures('init_web_driver')
class Test_web:

    def test_verify_login(self):
        WebFlows.login_flow(get_data('Username'), get_data('Password'))
        WebFlows.verify_title("Products")

    def test_verify_menu_buttons(self):
        WebFlows.verify_menu_buttons_flow()

    def test_verify_products(self):
        WebFlows.verifiy_products_names_and_desc()

    def test_verify_product_page(self):
        WebFlows.verify_product_page_details()

    def test_cart(self):
        WebFlows.add_and_verifiy_product_in_cart(r_ID)

    def test_checkout(self):
        WebFlows.checkout_proccess("test1","test2","1231")


    # upcoming tests
    # def test_logout(self):
    # def test_login_diffrent_user

    #def teardown_method(self):
        #WebFlows.return_home()

