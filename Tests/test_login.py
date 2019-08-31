from Fixture.HomePage import HomePage
from Fixture.LoginPage import LoginPage
from Fixture.MyAccountPage import MyAccountPage
import pytest
import unittest
import time
from ddt import ddt,data,unpack


@pytest.mark.usefixtures('store')
@ddt
class LoginPage(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def object_setup(self, store):
        self.home_page = HomePage(store)
        self.login_page = LoginPage(store)
        self.my_account_page = MyAccountPage(store)

    @pytest.mark.positive
    def test_login(self):
        self.home_page.open()\
            .click_on_sign_in_button()
        self.login_page.enter_login(login="automation@acemail.info")\
            .enter_password(password="password")\
            .click_submit_button()
        assert self.my_account_page.header_user_info_text() == "Auto Test"

    @data(('automation@acemail.info', ''),
          ('automation@acemail.info', ' '))
    @unpack
    def test_login_without_password(self, login, password):
        self.home_page.clear_cookies()\
            .open()\
            .click_on_sign_in_button()
        self.login_page.enter_login(login=login) \
            .enter_password(password=password) \
            .click_submit_button()
        assert self.login_page.error_message() == "Password is required."
