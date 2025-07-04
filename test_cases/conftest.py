import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from utilities.common_ops import get_data, get_time_stamp
from utilities.event_listener import EventListener
from utilities.manage_pages import ManagePages
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver

driver = None
action = None


@pytest.fixture(scope='class')
def init_web_driver(request):
    edriver = get_web_driver()
    globals()['driver'] = EventFiringWebDriver(edriver, EventListener())
    driver.maximize_window()
    driver.implicitly_wait(int(get_data("WaitTime")))
    driver.get(get_data('URL'))
    request.cls.driver = driver
    globals()['action'] = ActionChains(driver)
    ManagePages.init_web_pages()
    yield
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
    chrome_options = Options()
    chrome_options.add_argument('--disable-save-password-bubble')
    chrome_options.add_experimental_option('prefs', {
        'credentials_enable_service': False,
        'profile.password_manager_enabled': False,
        'profile.password_manager_leak_detection': False

    })
    chrome_driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    return chrome_driver


def get_firefox():
    firefox_driver = webdriver.Firefox(GeckoDriverManager().install())
    return firefox_driver


def get_edge():
    edge_driver = webdriver.Edge(EdgeChromiumDriverManager(log_level=20).install())  # log_level = 20 (bug fix)
    return edge_driver


# catch exection and take screenshot
def pytest_exception_interact(node, call, report):
    if report.failed:
        if globals()['driver'] is not None:
            screenshot = globals()['driver'].get_screenshot_as_png()
            allure.attach(
                screenshot,
                name=f"screenshot_{get_time_stamp()}",
                attachment_type=allure.attachment_type.PNG
            )