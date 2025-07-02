"""
Pytest configuration file to manage fixtures and hooks.
Includes WebDriver setup, teardown, and screenshot capture on test failure.
"""
# pylint: disable=redefined-outer-name
import datetime
import os
import pytest
from utils.driver_factory import Driverfactory
from utils.logger import get_logger


@pytest.fixture(scope="session")
def driver():
    """Fixture to initialise and return the WebDriver instance."""
    driver = Driverfactory.get_instance().get_driver()
    # already maximized in Driverfactory class
    #driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def logger():
    """Fixture to return the logger instance."""
    return get_logger()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    """capture screenshot on test failure."""
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver_fixture = item.funcargs.get("driver")
        if driver_fixture:
            screenshot_dir = os.path.join(os.getcwd(), "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = os.path.join(screenshot_dir, f"{timestamp}.png")
            driver_fixture.save_screenshot(filename)
