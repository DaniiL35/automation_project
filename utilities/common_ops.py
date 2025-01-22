from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import test_cases.conftest as conf
import xml.etree.ElementTree as ET


def get_data(node_name):
    root = ET.parse(r'/Users/danielshimon/PycharmProjects/automation_final_project/configuration/data.xml').getroot()
    return root.find(".//" + node_name).text


def wait(for_element, elem):
    if for_element == 'e lement_exist':
        WebDriverWait(conf.driver, int(get_data("WaitTime"))).until(EC.presence_of_element_located(elem))
    if for_element == 'element_displayed':
        WebDriverWait(conf.driver, int(get_data("WaitTime"))).until(EC.visibility_of_element_located(elem))


# enum for wait function
class For:
    ELEMENT_EXIST = 'element_exist'
    ELEMENT_DISPLAYED = 'element_displayed'
