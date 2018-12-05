import pytest

from src.factory.browser_factory import BrowserFactory


class TestGoogleHomePageTwo:
    driver = BrowserFactory.driver

    @pytest.mark.only
    def test_navigate_to_home_page_2(self):
        BrowserFactory.base_page.navigate_to_home_page() \
             .enter_text_and_search("Github") \
            # .click_on_the_first_link()

    @pytest.mark.only
    def test_navigate_to_home_page_3(self):
        BrowserFactory.base_page.navigate_to_home_page() \
             .enter_text_and_search("Github") \

    def teardown_method(self):
        if (self.driver != None):
            self.driver.quit()
