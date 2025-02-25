from smart_assertions import soft_assert, verify_expectations
from utilities.common_ops import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.common_ops import get_data


class Verifications:
    @staticmethod
    def verify_equals(expected, actual):
        assert expected == actual, f'Expected {expected} but got {actual}'
    #
    @staticmethod
    def is_displayed(element):
        assert element.is_displayed(), f'Element {element.text} is not displayed'

    def soft_assert(elems):
        timeout = int(get_data("softdisplayedtime"))  # get timeout from config file
        for elem in elems:
            try:
                WebDriverWait(elem.parent, timeout).until(EC.visibility_of(elem))
                soft_assert(elem.is_displayed(),
                            f'Element {elem.text} is not displayed, elem location: {elem.location}')
            except Exception as e:
                print(f"Exception while verifying element visibility: {e}")
                soft_assert(False, f'Element {elem.tag_name} failed visibility check')
        verify_expectations()

    @staticmethod
    def soft_displayed(elements):
        failed_elements = []
        timeout = int(get_data("softdisplayedtime"))

        for elem in elements:
            try:
                WebDriverWait(elem.parent, timeout).until(EC.visibility_of(elem))

                if not elem.is_displayed():
                    failed_elements.append(elem)
            except Exception as e:
                print(f"Exception while verifying element visibility: {e}")
                failed_elements.append(elem)

        if failed_elements:
            for elem in failed_elements:
                print(
                    f'Soft display failed for element: {elem.tag_name} | Text: {elem.text} | Location: {elem.location}')
            raise AssertionError("Soft Display failed")
