from src.utilities.selenium_utility import SeleniumUtility


class ResultsPage:
    def __init__(self, driver):
        self.driver = driver
        self.selenium_utility_handle = SeleniumUtility(driver)

    def click_on_the_first_link(self):
        pass
