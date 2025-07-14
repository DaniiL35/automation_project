import allure
import test_cases.conftest as conf
from extensions.ui_actions import UiActions

class Mobile_Actions(UiActions):
    @staticmethod
    @allure.step("Tap on element")
    def tap(elem, times=1):
        """
        Tap an element multiple times.
        """
        actions = conf.action_builder
        finger = conf.finger

        for _ in range(times):
            actions.w3c_actions.pointer_action.move_to(origin=elem, x=0, y=0)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pointer_up()

        actions.perform()

    @staticmethod
    @allure.step("Swipe from point to point")
    def swipe(start_x, start_y, end_x, end_y, duration=500):
        """
        Swipe from one coordinate to another.
        """
        actions = conf.action_builder
        finger = conf.finger

        actions.w3c_actions.pointer_action.move_to(x=start_x, y=start_y, origin="viewport")
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to(x=end_x, y=end_y, duration=duration, origin="viewport")
        actions.w3c_actions.pointer_action.pointer_up()
        actions.perform()

    @staticmethod
    @allure.step("Zoom on element")
    def zoom(elem, pixels=200, duration=500):
        driver = conf.driver

        finger1 = conf.create_new_finger("finger1")
        finger2 = conf.create_new_finger("finger2")

        x = elem.rect['x'] + (elem.rect['width'] // 2)
        y = elem.rect['y'] + (elem.rect['height'] // 2)

        builder = conf.create_action_builder(driver, finger1, finger2)

        # Start fingers at center
        builder.w3c_actions.pointer_action.move_to(origin="viewport", x=x, y=y)
        builder.w3c_actions.pointer_action.pointer_down()
        builder.w3c_actions.pointer_action2.move_to(origin="viewport", x=x, y=y)
        builder.w3c_actions.pointer_action2.pointer_down()

        # Move fingers apart
        builder.w3c_actions.pointer_action.move_to(origin="viewport", x=x - pixels, y=y, duration=duration)
        builder.w3c_actions.pointer_action2.move_to(origin="viewport", x=x + pixels, y=y, duration=duration)

        builder.w3c_actions.pointer_action.pointer_up()
        builder.w3c_actions.pointer_action2.pointer_up()

        builder.perform()

    @staticmethod
    @allure.step("Pinch on element")
    def pinch(elem, pixels=200, duration=500):
        driver = conf.driver

        finger1 = conf.create_new_finger("finger1")
        finger2 = conf.create_new_finger("finger2")

        x = elem.rect['x'] + (elem.rect['width'] // 2)
        y = elem.rect['y'] + (elem.rect['height'] // 2)

        builder = conf.create_action_builder(driver, finger1, finger2)

        # Start fingers apart
        builder.w3c_actions.pointer_action.move_to(origin="viewport", x=x - pixels, y=y)
        builder.w3c_actions.pointer_action.pointer_down()
        builder.w3c_actions.pointer_action2.move_to(origin="viewport", x=x + pixels, y=y)
        builder.w3c_actions.pointer_action2.pointer_down()

        # Move fingers toward center
        builder.w3c_actions.pointer_action.move_to(origin="viewport", x=x, y=y, duration=duration)
        builder.w3c_actions.pointer_action2.move_to(origin="viewport", x=x, y=y, duration=duration)

        builder.w3c_actions.pointer_action.pointer_up()
        builder.w3c_actions.pointer_action2.pointer_up()

        builder.perform()
