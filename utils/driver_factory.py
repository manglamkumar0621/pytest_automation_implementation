from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Driverfactory(object):
    __instance = None

    def __init__(self):
        if Driverfactory.__instance is not None:
            raise Exception("Singleton already created")
        else:
            self._driver = None
            Driverfactory.__instance = self

    @staticmethod
    def get_instance():
        if Driverfactory.__instance is None:
            Driverfactory()
        return Driverfactory.__instance

    def get_driver(self):
        if self._driver is None:
            options = Options()
            options.add_argument("--start-maximized")
            self._driver = webdriver.Chrome(options=options)
        return self._driver

