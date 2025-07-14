import csv
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import test_cases.conftest as conf
import xml.etree.ElementTree as ET
from pathlib import Path
import os




from pathlib import Path
import xml.etree.ElementTree as ET

def get_data(node_name, file_name='data.xml'):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(BASE_DIR, "configuration", file_name)
    root = ET.parse(file_path).getroot()
    return root.find(f".//{node_name}").text


# function to read csv files
def read_csv(file_name):
    data = []
    with open(file_name, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data


def get_time_stamp():
    return time.time()


def get_url():
    return conf.driver.current_url


def wait(for_element, elem):
    if for_element == 'element_exist':
        WebDriverWait(conf.driver, int(get_data("WaitTime"))).until(EC.presence_of_element_located(elem))
    if for_element == 'element_displayed':
        WebDriverWait(conf.driver, int(get_data("WaitTime"))).until(EC.visibility_of_element_located(elem))


# enum for wait function
class For:
    ELEMENT_EXIST = 'element_exist'
    ELEMENT_DISPLAYED = 'element_displayed'


# enum for save options
class save:
    Yes = 'yes'
    No = 'no'


# enum for swipe directions
class direction:
    left = 'left'
    right = 'right'
    up = 'up'
    down = 'down'
