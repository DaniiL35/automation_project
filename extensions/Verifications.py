class Verifications:
    @staticmethod
    def verify_equals(expected, actual):
        assert expected == actual, f'Expected {expected} but got {actual}'

    @staticmethod
    def is_displayed(element):
        assert element.is_displayed(), f'Element {element.text} is not displayed'

    @staticmethod
    def soft_displayed(elements):
        failed_elements = []
        for i in len(elements):
            if not elements[i].is_displayed():
                failed_elements.insert(len(failed_elements), elements[i])