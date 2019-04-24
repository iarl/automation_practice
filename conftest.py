from Fixture.Application import Application
import pytest


@pytest.fixture(scope="session")
def store(request):
    fixture = Application(browser=request.config.getoption("--browser"),
                          base_url=request.config.getoption("--base-url"))
    request.addfinalizer(fixture.destroy)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="Chrome", help="select browser: Chrome/Firefox")
    parser.addoption("--base-url", action='store', default='http://automationpractice.com/index.php', help="enter url")

