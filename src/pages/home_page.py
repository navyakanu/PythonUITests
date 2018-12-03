import time

from src.pages.results_page import ResultsPage
from src.utilities.selenium_utility import SeleniumUtility


class HomePage:
    def __init__(self, url, driver):
        driver.get(url)
        self.driver = driver
        self.url = url
        self.selenium_utility_handle = SeleniumUtility(driver)

        self.__ENTER_TEXT = "input[name='q']"
        self.__SEARCH_BUTTON = "input[value='Google Search']"

    def enter_text_and_search(self,search_for):
        self.selenium_utility_handle.wait_until_element_is_located(self.__ENTER_TEXT)
        self.selenium_utility_handle.enter_text(self.__ENTER_TEXT,search_for)
        self.selenium_utility_handle.click_button(self.__SEARCH_BUTTON)
        time.sleep(2)
        return ResultsPage(self.driver)
