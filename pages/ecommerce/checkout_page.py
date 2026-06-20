from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    CANCEL_BTN = (By.ID, "cancel")
    ERROR_MSG = (By.CSS_SELECTOR, "[data-test='error']")

    SUMMARY_ITEMS = (By.CLASS_NAME, "cart_item")
    ITEM_TOTAL = (By.CLASS_NAME, "summary_subtotal_label")
    TAX = (By.CLASS_NAME, "summary_tax_label")
    TOTAL = (By.CLASS_NAME, "summary_total_label")
    FINISH_BTN = (By.ID, "finish")

    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    BACK_HOME_BTN = (By.ID, "back-to-products")

    def fill_info(self, first_name, last_name, postal_code):
        self.type_text(*self.FIRST_NAME, first_name)
        self.type_text(*self.LAST_NAME, last_name)
        self.type_text(*self.POSTAL_CODE, postal_code)
        self.click(*self.CONTINUE_BTN)
        return self

    def get_error(self):
        return self.get_text(*self.ERROR_MSG)

    def get_item_total(self):
        text = self.get_text(*self.ITEM_TOTAL)
        return float(text.split("$")[1])

    def get_tax(self):
        text = self.get_text(*self.TAX)
        return float(text.split("$")[1])

    def get_total(self):
        text = self.get_text(*self.TOTAL)
        return float(text.split("$")[1])

    def finish(self):
        self.click(*self.FINISH_BTN)

    def get_confirmation_text(self):
        return self.get_text(*self.COMPLETE_HEADER)

    def back_home(self):
        self.click(*self.BACK_HOME_BTN)
