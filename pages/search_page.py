"""SearchPage encapsulates add-to-cart and checkout actions"""
import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SearchPage(BasePage):
    """Implements add-to-cart and checkout actions"""
    __FIRST_PRODUCT = (By.ID, "add-to-cart-sauce-labs-backpack")
    __GO_TO_CART = (By.CLASS_NAME, 'shopping_cart_link')
    __CHECKOUT = (By.ID, 'checkout')

    def add_first_product(self):
        """Select the first product on the search page"""
        time.sleep(3)
        self.click(self.__FIRST_PRODUCT)
        #self._driver.switch_to.window(self._driver.window_handles[1])
        return self

    def go_to_cart(self):
        """Click on the add-to-cart button"""
        time.sleep(2)
        return self.click(self.__GO_TO_CART)

    def checkout(self):
        """Search for product and open first result."""
        return self.click(self.__CHECKOUT)

    def add_to_cart_and_checkout(self):
        """Click on add to cart."""
        return self.add_first_product().go_to_cart().checkout()
