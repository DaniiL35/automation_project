import test_cases.conftest as conf


class UiActions:
    @staticmethod
    def click(element):
        element.click()

    @staticmethod
    def input_text(element, text):
        element.send_keys(text)

    @staticmethod
    def mouse_hover(element1, element2):
        conf.action.move_to_element(element1).move_to_element(element2).click.perform()

    @staticmethod
    def right_click(element):
        conf.action.context_click(element).perform()

    @staticmethod
    def double_click(element):
        conf.action.double_click(element).perform()

    @staticmethod
    def drag_and_drop(element1, element2):
        conf.action.drag_and_drop(element1, element2).perform()

    @staticmethod
    def clear(element):
        element.clear()
