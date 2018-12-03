from time import sleep

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import ui
from selenium.webdriver.support.wait import WebDriverWait


class SeleniumUtility:
    def __init__(self, driver):
        self.driver = driver

    def wait_until_element_is_located(self, css_path):
        wait = WebDriverWait(self.driver, 60)
        wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, css_path)))

    def find_element(self, css_path):
        self.wait_until_element_is_located(css_path)
        if self.is_visible(css_path):
            element = self.driver.find_element_by_css_selector(css_path)
        else:
            raise ElementNotVisible("Element with css path :::: {0}  :: is not visible".format(css_path))

        return element

    def click_button(self, css_path):
        self.wait_until_element_is_located(css_path)
        webelement = self.find_element(css_path)
        WebDriverWait(self.driver, 60).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, css_path)))
        webelement.click()
        sleep(2)

    def is_visible(self, locator, timeout=60):
        try:
            ui.WebDriverWait(self.driver, timeout).until(
                expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locator)))
            return True
        except TimeoutException:
            return False

    def enter_text(self, css_path, text):

        webelement = self.find_element(css_path)
        webelement.clear()
        webelement.send_keys(text)
        sleep(5)


class PageNotLoadedError(Exception):
    def __init__(self, message):
        self.message = message


class ElementNotVisible(Exception):
    def __init__(self, message):
        self.message = message


class ServiceNotWorking(Exception):
    def __init__(self, message):
        self.message = message


class UserNotAuthorized(Exception):
    def __init__(self):
        self.message = "401 - User Not authorized"


class RetryError(Exception):
    def __init__(self):
        self.message = "Retry failed"
