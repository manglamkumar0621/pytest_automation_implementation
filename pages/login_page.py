"""LoginPage encapsulates the login steps on the Amazon login page."""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.config import BASE_URL


class LoginPage(BasePage):
    """Implements the login page methods."""
    __EMAIL = (By.ID, "user-name")
    __PASSWORD = (By.ID, "password")
    __SIGN_IN = (By.ID, "login-button")

    def load_login_page(self):
        """Loads the Saucedemo login page."""
        self._driver.get(BASE_URL)
        return self

    def enter_email(self, email):
        """enters the email"""
        return self.send_keys(self.__EMAIL, email)

    def enter_password(self, password):
        """enters the password"""
        return self.send_keys(self.__PASSWORD, password)

    def click_sign_in(self):
        """clicks the sign-in button"""
        self.click(self.__SIGN_IN)

    def login(self, email, password):
        """Complete the login process using email and password."""
        return (self.enter_email(email)
                .enter_password(password)
                .click_sign_in())
