from extensions.ui_actions import UiActions


class WebFlows:

    @staticmethod
    def login_flow(username, password):
        UiActions.input_text('username', username)
        UiActions.input_text('password', password)
        UiActions.click('login_button')



