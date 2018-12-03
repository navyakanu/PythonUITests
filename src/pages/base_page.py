import logging

from src.pages.home_page import HomePage


class BasePage:
    def __init__(self, url, driver):
        self.driver = driver
        self.url = url
        self.logger = logging.getLogger("Login page")

    def navigate_to_home_page(self):
        self.logger.info("Opening google page")
        return HomePage(self.url, self.driver)
