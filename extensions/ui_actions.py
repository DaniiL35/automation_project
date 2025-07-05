import allure
import test_cases.conftest as conf


class UiActions:

    @staticmethod
    @allure.step('click on element')
    def click(element):
        element.click()

    @staticmethod
    @allure.step('input text into element')
    def input_text(element, text):
        element.send_keys(text)

    @staticmethod
    @allure.step('mouse hover over two elements')
    def mouse_hover(element1, element2):
        conf.action.move_to_element(element1).move_to_element(element2).click.perform()

    @staticmethod
    @allure.step('right click on element')
    def right_click(element):
        conf.action.context_click(element).perform()

    @staticmethod
    @allure.step('double click on element')
    def double_click(element):
        conf.action.double_click(element).perform()

    @staticmethod
    @allure.step('drag and drop element1 to element2')
    def drag_and_drop(element1, element2):
        conf.action.drag_and_drop(element1, element2).perform()

    @staticmethod
    @allure.step('clear element text')
    def clear(element):
        element.clear()
