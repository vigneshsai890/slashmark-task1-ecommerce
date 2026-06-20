import pytest
from pages.ecommerce.login_page import LoginPage
from pages.ecommerce.products_page import ProductsPage
from pages.ecommerce.cart_page import CartPage


@pytest.mark.ecommerce
class TestCart:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        LoginPage(driver).open().login("standard_user", "secret_sauce")
        self.products = ProductsPage(driver)
        self.cart = CartPage(driver)

    def test_add_single_item(self, driver):
        self.products.add_to_cart_by_index(0)
        assert self.products.get_cart_count() == 1

    def test_add_multiple_items(self, driver):
        self.products.add_to_cart_by_name("sauce-labs-backpack")
        self.products.add_to_cart_by_name("sauce-labs-bike-light")
        self.products.add_to_cart_by_name("sauce-labs-bolt-t-shirt")
        assert self.products.get_cart_count() == 3

    def test_remove_item_from_products_page(self, driver):
        self.products.add_to_cart_by_name("sauce-labs-backpack")
        self.products.add_to_cart_by_name("sauce-labs-bike-light")
        self.products.remove_from_cart_by_name("sauce-labs-backpack")
        assert self.products.get_cart_count() == 1

    def test_cart_shows_correct_items(self, driver):
        self.products.add_to_cart_by_name("sauce-labs-backpack")
        self.products.add_to_cart_by_name("sauce-labs-bolt-t-shirt")
        self.products.go_to_cart()
        items = self.cart.get_item_names()
        assert "Sauce Labs Backpack" in items
        assert "Sauce Labs Bolt T-Shirt" in items
        assert self.cart.get_item_count() == 2

    def test_remove_item_from_cart_page(self, driver):
        self.products.add_to_cart_by_name("sauce-labs-backpack")
        self.products.add_to_cart_by_name("sauce-labs-bike-light")
        self.products.go_to_cart()
        self.cart.remove_item(0)
        assert self.cart.get_item_count() == 1

    def test_continue_shopping(self, driver):
        self.products.go_to_cart()
        self.cart.continue_shopping()
        assert self.products.get_page_title() == "Products"

    def test_empty_cart(self, driver):
        self.products.go_to_cart()
        assert self.cart.get_item_count() == 0
