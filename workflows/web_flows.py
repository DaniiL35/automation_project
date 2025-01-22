import page_objects.web_objects.inventory_page as inv_pg
import utilities.common_ops
from extensions.ui_actions import UiActions
import utilities.manage_pages as page
from extensions.Verifications import Verifications
from utilities.common_ops import For


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
