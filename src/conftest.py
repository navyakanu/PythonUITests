import pytest
from selenium import webdriver

from src.pages.base_page import BasePage
from src.utilities.config_setup import ConfigSetup


def pytest_addoption(parser):
    parser.addoption("--withdocker", action="store", default=False,
                     help="specify if tests need to be run in dockerised Selenium hub")


@pytest.fixture(scope='class')
def withdocker(request):
    return request.config.option.withdocker


@pytest.fixture(params=["chrome_62","chrome","firefox"], scope="class")
def create_driver(request):
    __config = ConfigSetup()
    url = __config.get_base_url()
    if request.param == "chrome":
        capabilities = {
            "browserName": "chrome",
            "version": "61.0",
            "enableVNC": True,
            "enableVideo": True
        }
    if request.param == "firefox":
        capabilities = {
            "browserName": "firefox",
            "enableVNC": True,
            "enableVideo": True,
            "version": "47.0"
        }

    if request.param == "chrome_62":
        capabilities = {
            "browserName": "chrome",
            "enableVNC": True,
            "enableVideo": True,
            "version": "62.0"
        }

    web_driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            desired_capabilities=capabilities)

    request.cls.driver = web_driver
    request.cls.base_page = BasePage(url, web_driver)
    yield
    if web_driver != None:
        web_driver.quit()
