"""Testcase to automate Sauce login, search and add-to-cart"""
import pytest

from conftest import driver, logger
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.search_page import SearchPage
from utils import config


class TestSaucedemoCartFlow:

    def test_saucedemo_login(self, driver, logger):
        """Test Sauce login, search product and add-to-cart."""
        logger.info("Logging in Saucedemo page")
        (LoginPage(driver)
         .load_login_page()
         .login(config.EMAIL, config.PASSWORD))
        logger.info("Successfully logged in Saucedemo page")

    def test_saucedemo_add_item_to_cart(self,driver,logger):
        logger.info("Searching for product and adding first search result to cart")
        (SearchPage(driver).
         add_to_cart_and_checkout())
        logger.info
