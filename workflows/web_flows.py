import time

import page_objects.web_objects.inventory_page as inv_pg
import utilities.common_ops
from extensions.ui_actions import UiActions
import utilities.manage_pages as page
from extensions.Verifications import Verifications
from utilities.common_ops import get_data as GD, read_csv as RC, For


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
        for i in range(len(products_names)):  # Iterate through products
            expected_name = data[i]["Product Name"].strip()
            expected_desc = data[i]["Product Description"].strip()
            # Compare UI with CSV
            Verifications.verify_equals(expected_name, products_names[i].text.strip())
            Verifications.verify_equals(expected_desc, products_desc[i].text.strip())

    @staticmethod
    def verify_product_page_details():
        products_list = page.web_inventory.get_products()
        for i in range(len(products_list)):
            expected_name = data[i]["Product Name"].strip()
            expected_desc = data[i]["Product Description"].strip()
            expected_price = data[i]["Product Price"].strip()
            UiActions.click((products_list[i]))
            p_name = page.product_page.get_product_title().text
            p_desc = page.product_page.get_product_description().text
            p_price = page.product_page.get_product_price().text
            Verifications.verify_equals(expected_name, p_name)
            Verifications.verify_equals(expected_desc, p_desc)
            Verifications.verify_equals(expected_price, p_price)
            UiActions.click(page.product_page.get_back_to_products())
            products_list = page.web_inventory.get_products()

    @staticmethod
    def add_and_verifiy_product_in_cart(ID):
        products_list = page.web_inventory.get_products()
        UiActions.click((products_list[ID]))
        UiActions.click(page.product_page.get_buy_button())
        UiActions.click(page.web_upper_menu.get_cart_icon())
        names = page.cart_page.get_items_names()
        Verifications.verify_equals(names[0].text, data[ID]["Product Name"].strip())

    @staticmethod
    def checkout_proccess(firstname, lastname, postalcode):
        if utilities.common_ops.get_url() == GD('CartURL'):
            UiActions.click(page.cart_page.get_checkout_button())
        UiActions.input_text(page.checkout_page.get_first_name_field(), firstname)
        UiActions.input_text(page.checkout_page.get_last_name_field(), lastname)
        UiActions.input_text(page.checkout_page.get_postal_code_field(), postalcode)
        UiActions.click(page.checkout_page.get_continue_button())
        UiActions.click(page.overview_page.get_finish_button())
        Verifications.verify_equals(utilities.common_ops.get_url(), GD("CheckoutCompleteURL"))

    @staticmethod
    def return_home():
        UiActions.click(page.web_upper_menu.get_burger_menu())
        UiActions.click(page.web_upper_menu.get_all_items())
        UiActions.click(page.web_upper_menu.get_close_button())
        time.sleep(2)


data = RC(GD("csvfile"))
