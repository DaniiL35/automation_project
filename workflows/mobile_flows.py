import allure
from extensions.Verifications import Verifications
from extensions.mobile_actions import Mobile_Actions
import utilities.manage_pages as page
import test_cases.conftest as conf
from utilities.common_ops import get_data


class MobileFlows():

    @staticmethod
    @allure.step('fill in mortgage details flow')
    def mortgage_flow(amount, term, rate, save):
        MobileActions.update_text(page.mobile_calculator.get_amount(), amount)
        Mobile_Actions.update_text(page.mobile_calculator.get_term(), term)
        Mobile_Actions.update_text(page.mobile_calculator.get_rate(), rate)
        Mobile_Actions.click(page.mobile_calculator.get_calculate_button())
        if save:
            Mobile_Actions.click(page.mobile_calculator.get_save_button())

    @staticmethod
    @allure.step('verify repayment flow ')
    def verify_mortgage_repayment(expected):
        actual = page.mobile_calculator.get_repayment().text
        Verifications.verify_equals('£' + expected, actual)

    @staticmethod
    @allure.step('swipe screen')
    def swipe_screen(direction):
        width = conf.mobile_size['width']
        height = conf.mobile_size['height']
        start_x, start_y, end_x, end_y = 0, 0, 0, 0
        if direction == 'left':
            start_x = width * 0.9
            end_x = width * 0.1
            start_y = end_y = height / 2

        if direction == 'right':
            start_x = width * 0.1
            end_x = width * 0.9
            start_y = end_y = height / 2

        if direction == 'up':
            start_y = height * 0.9
            end_y = height * 0.1
            start_x = end_x = width / 2

        if direction == 'down':
            start_y = height * 0.1
            end_y = height * 0.9
            start_x = end_x = width / 2
        Mobile_Actions.swipe(start_x, start_y, end_x, end_y, int(get_data("Swipe_Duration")))

    @staticmethod
    @allure.step('verify and delete saved mortgage')
    def verify_rate_delete_transaction(expected):
        actual_rate = page.mobile_calculator.get_rate.text
        Verifications.verify_equals(f'{expected}%', actual_rate)
        Mobile_Actions.click(page.mobile_calculator.get_delete_button(), 1)
        Mobile_Actions.click(page.mobile_calculator.get_confirm_delete_button(), 1)
