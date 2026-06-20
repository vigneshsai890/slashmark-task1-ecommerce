import pytest
from pages.ecommerce.login_page import LoginPage
from pages.ecommerce.products_page import ProductsPage
from pages.ecommerce.cart_page import CartPage
from pages.ecommerce.checkout_page import CheckoutPage


@pytest.mark.ecommerce
class TestCheckout:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        LoginPage(driver).open().login("standard_user", "secret_sauce")
        self.products = ProductsPage(driver)
        self.cart = CartPage(driver)
        self.checkout = CheckoutPage(driver)

    def _add_item_and_go_to_checkout(self):
        self.products.add_to_cart_by_name("sauce-labs-backpack")
        self.products.go_to_cart()
        self.cart.checkout()

    @pytest.mark.smoke
    def test_complete_checkout(self, driver):
        self._add_item_and_go_to_checkout()
        self.checkout.fill_info("John", "Doe", "12345")
        self.checkout.finish()
        assert self.checkout.get_confirmation_text() == "Thank you for your order!"

    def test_checkout_total_matches_cart(self, driver):
        try:
            self.products.add_to_cart_by_name("sauce-labs-backpack")
            self.products.add_to_cart_by_name("sauce-labs-bike-light")
            self.products.go_to_cart()
            cart_total = self.cart.get_total_price()
            self.cart.checkout()
            self.checkout.fill_info("Jane", "Smith", "67890")
            assert self.checkout.get_item_total() == cart_total
        except Exception as e:
            print("URL:", driver.current_url)
            driver.save_screenshot("screenshots/debug_checkout.png")
            raise e

    def test_tax_calculated(self, driver):
        self._add_item_and_go_to_checkout()
        self.checkout.fill_info("Test", "User", "00000")
        assert self.checkout.get_tax() > 0

    def test_total_equals_subtotal_plus_tax(self, driver):
        self._add_item_and_go_to_checkout()
        self.checkout.fill_info("Test", "User", "00000")
        subtotal = self.checkout.get_item_total()
        tax = self.checkout.get_tax()
        total = self.checkout.get_total()
        assert abs(total - (subtotal + tax)) < 0.01

    def test_checkout_missing_first_name(self, driver):
        self._add_item_and_go_to_checkout()
        self.checkout.fill_info("", "Doe", "12345")
        assert "First Name is required" in self.checkout.get_error()

    def test_checkout_missing_last_name(self, driver):
        self._add_item_and_go_to_checkout()
        self.checkout.fill_info("John", "", "12345")
        assert "Last Name is required" in self.checkout.get_error()

    def test_checkout_missing_postal_code(self, driver):
        self._add_item_and_go_to_checkout()
        self.checkout.fill_info("John", "Doe", "")
        assert "Postal Code is required" in self.checkout.get_error()

    def test_back_home_after_checkout(self, driver):
        self._add_item_and_go_to_checkout()
        self.checkout.fill_info("John", "Doe", "12345")
        self.checkout.finish()
        self.checkout.back_home()
        assert self.products.get_page_title() == "Products"


@pytest.mark.ecommerce
class TestCheckoutMultipleItems:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        LoginPage(driver).open().login("standard_user", "secret_sauce")
        self.products = ProductsPage(driver)
        self.cart = CartPage(driver)
        self.checkout = CheckoutPage(driver)

    @pytest.mark.parametrize("first,last,postal", [
        ("Alice", "Wonder", "10001"),
        ("Bob", "Builder", "90210"),
        ("Charlie", "Chaplin", "SW1A"),
    ])
    def test_checkout_with_different_users(self, driver, first, last, postal):
        self.products.add_to_cart_by_index(0)
        self.products.go_to_cart()
        self.cart.checkout()
        self.checkout.fill_info(first, last, postal)
        self.checkout.finish()
        assert self.checkout.get_confirmation_text() == "Thank you for your order!"
