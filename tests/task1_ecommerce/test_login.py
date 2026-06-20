import pytest
from pages.ecommerce.login_page import LoginPage
from pages.ecommerce.products_page import ProductsPage


@pytest.mark.ecommerce
class TestLogin:
    def test_valid_login(self, driver):
        LoginPage(driver).open().login("standard_user", "secret_sauce")
        assert ProductsPage(driver).get_page_title() == "Products"

    @pytest.mark.parametrize("username,password,expected_error", [
        ("locked_out_user", "secret_sauce", "Sorry, this user has been locked out"),
        ("invalid_user", "secret_sauce", "Username and password do not match"),
        ("standard_user", "wrong_pass", "Username and password do not match"),
        ("", "secret_sauce", "Username is required"),
        ("standard_user", "", "Password is required"),
    ])
    def test_invalid_login(self, driver, username, password, expected_error):
        login = LoginPage(driver).open()
        login.login(username, password)
        assert expected_error in login.get_error()

    def test_logout(self, driver):
        LoginPage(driver).open().login("standard_user", "secret_sauce")
        ProductsPage(driver).logout()
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        WebDriverWait(driver, 10).until(EC.url_contains("saucedemo.com"))
        assert "saucedemo.com" in driver.current_url
