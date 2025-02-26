import pytest

from utilities.common_ops import get_data
from utilities.manage_pages import web_upper_menu
from workflows.web_flows import WebFlows
import time


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

