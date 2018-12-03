import pytest

from src.factory.browser_factory import BrowserFactory


class TestGoogleHomePage:
    driver = BrowserFactory.driver

    @pytest.mark.only
    def test_navigate_to_home_page(self):
        BrowserFactory.base_page.navigate_to_home_page() \
             .enter_text_and_search("Github") \
            # .click_on_the_first_link()

    def teardown_method(self):
        self.driver.quit()
