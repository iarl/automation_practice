from BasePage import BasePage


class HomePage(BasePage):
    #locators
    _sign_in_button_locator = '//*[@class="login"]'

    def open(self):
        self._go_to_link(self.base_url)
        return self

    def click_on_sign_in_button(self):
        self._click_on_element(self._sign_in_button_locator)
        return self

