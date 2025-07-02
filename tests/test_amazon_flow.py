from pages.login_page import LoginPage
from pages.search_page import SearchPage
from utils import config


def test_amazon_cart_flow(driver, logger):
    LoginPage(driver).load_login_page().login(config.EMAIL, config.PASSWORD)
    SearchPage(driver).search_product(config.PRODUCT_NAME).add_to_cart()
