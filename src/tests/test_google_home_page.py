import pytest


@pytest.mark.usefixtures("create_driver")
class TestGoogleHomePage:

    @pytest.mark.only
    def test_navigate_to_home_page(self):
        self.base_page.navigate_to_home_page() \
             .enter_text_and_search("Github")
            # .click_on_the_first_link()

