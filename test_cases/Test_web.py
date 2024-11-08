import time
import pytest


@pytest.mark.usefixtures('init_web_driver')
class Test_web:

    def test_kuku(self):

        time.sleep(2)

