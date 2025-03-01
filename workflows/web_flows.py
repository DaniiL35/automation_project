import page_objects.web_objects.inventory_page as inv_pg
import utilities.common_ops
from extensions.ui_actions import UiActions
import utilities.manage_pages as page
from extensions.Verifications import Verifications
from utilities.common_ops import For
from utilities.common_ops import get_products_data as gd


class WebFlows:

    @staticmethod
    def login_flow(username, password):
        UiActions.input_text(page.web_login.get_username(), username)
        UiActions.input_text(page.web_login.get_password(), password)
        UiActions.click(page.web_login.get_login_button())

    @staticmethod
    def verify_title(expected):
        utilities.common_ops.wait(For.ELEMENT_DISPLAYED, inv_pg.title)
        actual = page.web_inventory.get_main_title().text
        Verifications.verify_equals(expected, actual)

    @staticmethod
    def verify_menu_buttons_flow():
        elems_closed = [
            page.web_upper_menu.get_cart_icon(),
            page.web_upper_menu.get_burger_menu(), ]
        elems_open = [
            page.web_upper_menu.get_all_items(),
            page.web_upper_menu.get_about(),
            page.web_upper_menu.get_logout(),
            page.web_upper_menu.get_reset()]
        Verifications.soft_assert_displayed(elems_closed)
        UiActions.click(page.web_upper_menu.get_burger_menu())
        Verifications.soft_assert_displayed(elems_open)
        UiActions.click(page.web_upper_menu.get_close_button())

    @staticmethod
    def verifiy_products_names_and_desc():
        products_names = page.web_inventory.get_products()
        products_desc = page.web_inventory.get_products_description()
        for i in range(len(products_names)):
            Verifications.soft_assert_equals(gd(f'productn{i + 1}'), products_names[i].text)
            Verifications.soft_assert_equals(gd(f'productd{i + 1}'), products_desc[i].text)

    @staticmethod
    def verify_product_page_details():
        products_list = page.web_inventory.get_products()
        for i in range(len(products_list)):
            UiActions.click((products_list[i]))
            p_name = page.product_page.get_product_title().text
            p_desc = page.product_page.get_product_description().text
            p_price = page.product_page.get_product_price().text
            Verifications.verify_equals(gd(f'productn{i+1}'), p_name)
            Verifications.verify_equals(gd(f'productd{i+1}'), p_desc)
            Verifications.verify_equals(gd(f'productp{i+1}'), p_price)
            UiActions.click(page.product_page.get_back_to_products())
            products_list = page.web_inventory.get_products()


