class Verifications:
    @staticmethod
    def verify_equals(expected, actual):
        assert expected == actual, f'Expected {expected} but got {actual}'

    @staticmethod
    def is_displayed(element):
        assert element.is_displayed(), f'Element {element.text} is not displayed'
