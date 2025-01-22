import pytest

from utilities.common_ops import get_data
from workflows.web_flows import WebFlows
import time


@pytest.mark.usefixtures('init_web_driver')
class Test_web:

    def test_verify_login(self):
        time.sleep(2)
        WebFlows.login_flow(get_data('Username'),get_data('Password'))
        WebFlows.verify_title("Products")
