import datetime
import os

import pytest
from selenium import webdriver

from utils.logger import get_logger


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def logger():
    return get_logger()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver_fixture = item.funcargs.get("driver")
        if driver_fixture:
            screenshot_dir = os.path.join(os.getcwd(), "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filname = os.path.join(screenshot_dir, f"{timestamp}.png")
            driver_fixture.save_screenshot(filname)
