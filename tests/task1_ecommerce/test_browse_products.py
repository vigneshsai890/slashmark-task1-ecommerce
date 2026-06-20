import pytest
from pages.ecommerce.login_page import LoginPage
from pages.ecommerce.products_page import ProductsPage


@pytest.mark.ecommerce
class TestBrowseProducts:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        LoginPage(driver).open().login("standard_user", "secret_sauce")
        self.products = ProductsPage(driver)

    def test_products_displayed(self, driver):
        assert self.products.get_product_count() == 6

    def test_product_names_not_empty(self, driver):
        names = self.products.get_product_names()
        assert all(len(name) > 0 for name in names)

    def test_product_prices_positive(self, driver):
        prices = self.products.get_product_prices()
        assert all(price > 0 for price in prices)

    def test_sort_price_low_to_high(self, driver):
        self.products.sort_by("lohi")
        prices = self.products.get_product_prices()
        assert prices == sorted(prices)

    def test_sort_price_high_to_low(self, driver):
        self.products.sort_by("hilo")
        prices = self.products.get_product_prices()
        assert prices == sorted(prices, reverse=True)

    def test_sort_name_a_to_z(self, driver):
        self.products.sort_by("az")
        names = self.products.get_product_names()
        assert names == sorted(names)

    def test_sort_name_z_to_a(self, driver):
        self.products.sort_by("za")
        names = self.products.get_product_names()
        assert names == sorted(names, reverse=True)

    def test_open_product_detail(self, driver):
        name = self.products.get_product_names()[0]
        self.products.open_product(0)
        assert name in driver.page_source
