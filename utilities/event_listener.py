from selenium.webdriver.support.events import AbstractEventListener


class EventListener(AbstractEventListener):
    button_text = None

    def before_navigate_to(self, url, driver):
        print("Before navigate to: {}".format(url))

    def after_navigate_to(self, url, driver):
        print("After navigate to: {}".format(url))

    def before_navigate_back(self, driver):
        print("Before navigate back: ", driver.current_url)

    def after_navigate_back(self, driver):
        print("After navigate back: ", driver.current_url)

    def before_navigate_forward(self, driver):
        print("Before navigate forward: ", driver.current_url)

    def after_navigate_forward(self, driver):
        print("After navigate forward: ", driver.current_url)

    def before_find(self, by, value, driver):
        print("Before find: ", driver.current_url)

    def after_find(self, by, value, driver):
        print("After find: ", driver.current_url)

    def before_change_value_of(self, element, driver):
        if element.tag_name == 'input':
            print("Before change value of:", element.get_attribute('value'))
        else:
            print("After change value of:", element.text)

    def after_change_value_of(self, element, driver):
        if element.tag_name == 'input':
            print("After change value of:", element.get_attribute('value'))
        else:
            print("After change value of:", element.text)

    def before_click(self, element, driver):
        if element.tag_name == 'input':
            text = element.get_attribute('value')
        else:
            text = element.text

        if not text:
            text = f"<no label for {element.tag_name}>"

        EventListener.button_text = text
        print("Before click: ", text)

    def after_click(self, element, driver):
        print("After click:", EventListener.button_text)

    def before_execute_script(self, driver):
        print("Before execute script", driver.current_url)

    def after_execute_script(self, driver):
        print("After execute script", driver.current_url)

    def before_close(self, driver):
        print("Before closing tab")

    def after_close(self, driver):
        print("After closing tab")

    def before_quit(self, driver):
        print("Before quit")

    def after_quit(self, driver):
        print("After quit")

    def on_exception(self, exception, driver):
        print("on_exception: " + str(exception))
