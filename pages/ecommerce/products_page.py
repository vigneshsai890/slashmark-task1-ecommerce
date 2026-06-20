from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class ProductsPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICES = (By.CLASS_NAME, "inventory_item_price")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    BURGER_MENU = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def get_page_title(self):
        return self.get_text(*self.TITLE)

    def get_product_count(self):
        return len(self.find_all(*self.INVENTORY_ITEMS))

    def get_product_names(self):
        items = self.find_all(*self.ITEM_NAMES)
        return [item.text for item in items]

    def get_product_prices(self):
        items = self.find_all(*self.ITEM_PRICES)
        return [float(p.text.replace("$", "")) for p in items]

    def add_to_cart_by_index(self, index):
        import time
        time.sleep(0.3)
        items = self.find_all(*self.INVENTORY_ITEMS)
        btn = items[index].find_element(By.CSS_SELECTOR, "button")
        self.driver.execute_script("arguments[0].click();", btn)
        time.sleep(0.5)
        return self

    def add_to_cart_by_name(self, product_name):
        btn_id = "add-to-cart-" + product_name.lower().replace(" ", "-")
        el = self.find(By.ID, btn_id)
        self.driver.execute_script("arguments[0].click();", el)
        import time
        time.sleep(0.5)
        return self

    def remove_from_cart_by_name(self, product_name):
        btn_id = "remove-" + product_name.lower().replace(" ", "-")
        el = self.find(By.ID, btn_id)
        self.driver.execute_script("arguments[0].click();", el)
        import time
        time.sleep(0.5)
        return self

    def get_cart_count(self):
        import time
        time.sleep(0.5)
        try:
            from selenium.webdriver.support import expected_conditions as EC
            self.wait.until(EC.visibility_of_element_located(self.CART_BADGE))
            return int(self.get_text(*self.CART_BADGE))
        except:
            return 0

    def go_to_cart(self):
        el = self.find(*self.CART_LINK)
        self.driver.execute_script("arguments[0].click();", el)

    def sort_by(self, option_value):
        dropdown = Select(self.find(*self.SORT_DROPDOWN))
        dropdown.select_by_value(option_value)

    def open_product(self, index):
        names = self.find_all(*self.ITEM_NAMES)
        names[index].click()

    def logout(self):
        el = self.find(*self.BURGER_MENU)
        self.driver.execute_script("arguments[0].click();", el)
        import time
        time.sleep(0.5)
        logout_el = self.find(*self.LOGOUT_LINK)
        self.driver.execute_script("arguments[0].click();", logout_el)
