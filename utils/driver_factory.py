"""Singleton DriverFactory class to manage single Webdriver instance."""
# pylint: disable=broad-exception-raised
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Driverfactory():
    """Driverfactory class to manage single Webdriver instance."""
    __instance = None

    def __init__(self):
        if Driverfactory.__instance is not None:
            raise Exception("Singleton already created")

        self._driver = None
        Driverfactory.__instance = self

    @staticmethod
    def get_instance():
        """Return the singleton instance of Driverfactory."""
        if Driverfactory.__instance is None:
            Driverfactory()
        return Driverfactory.__instance

    def get_driver(self):
        """Return the Chrome driver instance."""
        if self._driver is None:
            options = Options()
            options.add_argument("--start-maximized")
            self._driver = webdriver.Chrome(options=options)
        return self._driver
