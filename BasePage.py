from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class BasePage:

    def __init__(self, store):
        self.app = store
        self.base_url = store.base_url
        self.driver = store.driver

    def _go_to_link(self, url):
        self.driver.get(url)

    def _click_on_element(self, element_locator):
        self.driver.find_element_by_xpath(element_locator).click()

    def _fill_field(self, element_locator, text):
        element = self.driver.find_element_by_xpath(element_locator)
        element.click()
        element.clear()
        element.send_keys(text)

    def _get_element_text(self, element_locator):
        element = self.driver.find_element_by_xpath(element_locator)
        return element.text

    def _delete_cookies(self):
        self.driver.delete_all_cookies()

