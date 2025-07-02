"""Testcase to automate Amazon login, search and add-to-cart"""
from pages.login_page import LoginPage
from pages.search_page import SearchPage
from utils import config


def test_amazon_cart_flow(driver, logger):
    """Test Amazon login, search product and add-to-cart."""
    logger.info("Testing Amazon cart flow")
    logger.debug("Logging in Amazon page")
    (LoginPage(driver)
     .load_login_page()
     .login(config.EMAIL, config.PASSWORD))
    logger.info("Successfully logged in Amazon page")
    logger.debug("Searching for product and adding first search result to cart")
    (SearchPage(driver)
     .search_product(config.PRODUCT_NAME)
     .add_to_cart())
