import time
from selenium.webdriver import ActionChains
import pytest
from selenium import webdriver
from utilities.common_ops import get_data
from utilities.manage_pages import ManagePages
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = None
action = None


@pytest.fixture(scope='class')
def init_web_driver(request):
    globals()['driver'] = get_web_driver()
    driver.maximize_window()
    driver.implicitly_wait(int(get_data("WaitTime")))
    driver.get(get_data('URL'))
    request.cls.driver = driver
    globals()['action'] = ActionChains(driver)
    ManagePages.init_web_pages()
    yield
    time.sleep(2)  # should be removed
    driver.close()
    driver.quit()


def get_web_driver():
    web_driver = get_data('Browser')
    if web_driver.lower() == 'chrome':
        driver = get_chrome()
    elif web_driver.lower() == 'firefox':
        driver = get_firefox()
    elif web_driver.lower() == 'edge':
        driver = get_edge()
    else:
        driver = None
        raise Exception("Wrong Input, Unrecognized Browser")
    return driver


def get_chrome():
    chrome_driver = webdriver.Chrome(ChromeDriverManager().install())
    return chrome_driver


def get_firefox():
    firefox_driver = webdriver.Firefox(GeckoDriverManager().install())
    return firefox_driver


def get_edge():
    edge_driver = webdriver.Edge(EdgeChromiumDriverManager(log_level=20).install())  # log_level = 20 (bug fix)
    return edge_driver
