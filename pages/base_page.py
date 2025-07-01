from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    def __init__(self, driver):
        self._driver = driver

    def click(self, by_locator):
        (WebDriverWait(self._driver, 10)
         .until(EC.element_to_be_clickable(by_locator))
         .click())
        return self

    def send_keys(self, by_locator, text):
        (WebDriverWait(self._driver, 10)
         .until(EC.visibility_of_element_located(by_locator))
         .send_keys(text))
        return self

    def get_text(self, by_locator):
        # noinspection PyStatementEffect
        ((WebDriverWait(self._driver, 10)
         .until(EC.visibility_of_element_located(by_locator)))
         .text)
        return self
