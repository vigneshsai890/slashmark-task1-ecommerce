from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com"

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR_MSG = (By.CSS_SELECTOR, "[data-test='error']")

    def open(self):
        self.driver.get(self.URL)
        return self

    def login(self, username, password):
        self.type_text(*self.USERNAME, username)
        self.type_text(*self.PASSWORD, password)
        self.click(*self.LOGIN_BTN)
        return self

    def get_error(self):
        return self.get_text(*self.ERROR_MSG)

    def is_error_displayed(self):
        return self.is_visible(*self.ERROR_MSG)
