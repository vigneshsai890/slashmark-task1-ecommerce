from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICES = (By.CLASS_NAME, "inventory_item_price")
    ITEM_QUANTITY = (By.CLASS_NAME, "cart_quantity")
    CHECKOUT_BTN = (By.ID, "checkout")
    CONTINUE_SHOPPING = (By.ID, "continue-shopping")
    REMOVE_BTNS = (By.CSS_SELECTOR, "button[id^='remove-']")

    def get_cart_items(self):
        return self.find_all(*self.CART_ITEMS)

    def get_item_names(self):
        items = self.find_all(*self.ITEM_NAMES)
        return [item.text for item in items]

    def get_item_count(self):
        try:
            return len(self.find_all(*self.CART_ITEMS))
        except:
            return 0

    def get_total_price(self):
        prices = self.find_all(*self.ITEM_PRICES)
        return sum(float(p.text.replace("$", "")) for p in prices)

    def remove_item(self, index):
        btns = self.find_all(*self.REMOVE_BTNS)
        btn = btns[index]
        btn.click()
        from selenium.webdriver.support import expected_conditions as EC
        self.wait.until(EC.staleness_of(btn))

    def checkout(self):
        self.click(*self.CHECKOUT_BTN)

    def continue_shopping(self):
        self.click(*self.CONTINUE_SHOPPING)
