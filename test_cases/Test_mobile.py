import allure
import pytest
from utilities.common_ops import save, direction
from workflows.mobile_flows import MobileFlows


@pytest.mark.usefixtures("init_mobile_driver")
class Test_mobile:

    @allure.title('Test01: Verify mortgage repayment')
    @allure.step('this test verifies mortgage repayment')
    def test_verify_repayment(self):
        MobileFlows.mortgage_flow('1000', '5', '2.5', save.No)
        MobileFlows.verify_mortgage_repayment('18.06')


    @allure.title('Test02: Verify saved details')
    @allure.step('this test verifies saved transactions details')
    def test_saved_details(self):
        MobileFlows.mortgage_flow('1000', '5', '2.5', save.Yes)
        MobileFlows.swipe_screen(direction.left)
        MobileFlows.verify_rate_delete_transaction('2.5')
