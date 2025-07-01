from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.config import BASE_URL


class LoginPage(BasePage):
    __EMAIL = (By.ID, "ap_email")
    __PASSWORD = (By.ID, "ap_password")
    __SIGN_IN = (By.ID, "signInSubmit")
    __CONTINUE = (By.ID, "continue")

    def load_login_page(self):
        self._driver.get(BASE_URL)
        return self

    def enter_email(self, email):
        return self.send_keys(self.__EMAIL, email)

    def enter_password(self, password):
        return self.send_keys(self.__PASSWORD, password)

    def click_sign_in(self):
        self.click(self.__SIGN_IN)

    def click_continue(self):
        return self.click(self.__CONTINUE)

    def login(self, email, password):
        return (self.enter_email(email)
                .click_continue()
                .enter_password(password)
                .click_sign_in())
