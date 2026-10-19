import pytest

from pages.login import LoginPage
from utils.config import BASE_URL_UI
from data.users import UI_USER


@pytest.mark.ui
class TestLoginPage:

    def test_login_page(self, driver):
        driver.get(BASE_URL_UI)
        login_page = LoginPage(driver)
        login_page.set_username(UI_USER["username"])
        login_page.set_password(UI_USER["password"])

        assert login_page.get_username() == UI_USER["username"]

        login_page.click_login_button()

        assert "/inventory.html" in driver.current_url
