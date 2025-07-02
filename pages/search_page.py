"""SearchPage encapsulates search and add-to-cart actions"""
import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SearchPage(BasePage):
    """Implements search and add-to-cart actions"""
    __SEARCH_BOX = (By.ID, 'twotabsearchtextbox')
    __SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    __FIRST_PRODUCT = (By.CSS_SELECTOR, "div[data-index='1'] h2 a")
    __ADD_TO_CART = (By.ID, 'add-to-cart-button')

    def enter_search_term(self, product):
        """Enter the search term"""
        return self.send_keys(self.__SEARCH_BOX, product)

    def click_search(self):
        """Click search button"""
        return self.click(self.__SEARCH_BTN)

    def click_first_product(self):
        """Select the first product on the search page"""
        time.sleep(3)
        self.click(self.__FIRST_PRODUCT)
        self._driver.switch_to.window(self._driver.window_handles[1])
        return self

    def click_add_to_cart(self):
        """Click on the add-to-cart button"""
        time.sleep(2)
        return self.click(self.__ADD_TO_CART)

    def search_product(self, product):
        """Search for product and open first result."""
        return self.enter_search_term(product).click_search().click_first_product()

    def add_to_cart(self):
        """Click on add to cart."""
        return self.click_add_to_cart()
