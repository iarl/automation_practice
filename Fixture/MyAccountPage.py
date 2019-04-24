from BasePage import BasePage


class MyAccountPage(BasePage):
    #locators
    _header_user_info_locator = '//*[@class="header_user_info"]//span'
    _logout_button_locator = '//*[@class="logout"]'

    def header_user_info_text(self):
        return self._get_element_text(self._header_user_info_locator)

    def click_on_sign_out_button(self):
        self._click_on_element(self._logout_button_locator)
        return self

