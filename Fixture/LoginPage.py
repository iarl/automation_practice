from BasePage import BasePage


class LoginPage(BasePage):
    # locators
    _email_field_locator = '//*[@id="email"]'
    _password_field_locator = '//*[@id="passwd"]'
    _submit_button_locator = '//*[@id="SubmitLogin"]'
    _error_message_locator = '//*[@class="alert alert-danger"]//li'

    def enter_login(self, login):
        self._fill_field(self._email_field_locator, login)
        return self

    def enter_password(self, password):
        self._fill_field(self._password_field_locator, password)
        return self

    def click_submit_button(self):
        self._click_on_element(self._submit_button_locator)
        return self

    def error_message(self):
        return self._get_element_text(self._error_message_locator)

