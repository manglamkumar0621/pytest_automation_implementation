"""BasePage implements common methods for page actions like click, send_keys and get_text.
Supports method chaining"""
#pylint: disable=expression-not-assigned
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    """Create a BasePage object and pass driver object as parameter"""
    def __init__(self, driver):
        self._driver = driver

    def click(self, by_locator):
        """Click element by locator"""
        (WebDriverWait(self._driver, 10)
         .until(EC.element_to_be_clickable(by_locator))
         .click())
        return self

    def send_keys(self, by_locator, text):
        """Send text by locator"""
        (WebDriverWait(self._driver, 10)
         .until(EC.visibility_of_element_located(by_locator))
         .send_keys(text))
        return self

    def get_text(self, by_locator):
        """Get text by locator"""
        # noinspection PyStatementEffect
        ((WebDriverWait(self._driver, 10)
         .until(EC.visibility_of_element_located(by_locator)))
         .text)
        return self
