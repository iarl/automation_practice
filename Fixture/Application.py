from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver


class Application:
    def __init__(self, browser, base_url,):
        self.browser = browser
        self.base_url = base_url
        self.driver = self.choose_browser(browser)
        self.driver.maximize_window()
        self.driver.implicitly_wait(15)

    @staticmethod
    def choose_browser(browser):
        webdrivers = {'Chrome':
                          {'driver': webdriver.Chrome,
                           'manager': ChromeDriverManager},
                      'Firefox':
                          {'driver': webdriver.Firefox,
                           'manager': GeckoDriverManager}}
        driver = webdrivers[browser]['driver'](executable_path=webdrivers[browser]['manager']().install())
        return driver

    def destroy(self):
        self.driver.quit()

