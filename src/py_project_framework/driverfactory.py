from abc import ABC, abstractmethod
from selenium import webdriver


class Driver(ABC):
    @abstractmethod
    def get_driver(self):
        pass


class EdgeDriver(Driver):

    def get_driver(self):
        edge_options = webdriver.EdgeOptions()
        edge_options.add_argument('--start-maximized')
        return webdriver.Edge(edge_options)


class FirefoxDriver(Driver):

    def get_driver(self):
        ff_options = webdriver.FirefoxOptions()
        ff_options.add_argument('--start-maximized')
        return webdriver.Firefox()


class DriverFactory:

    def get_driver(self, browser_name):
        if browser_name == 'edge':
            return EdgeDriver().get_driver()
        elif browser_name == 'firefox':
            return FirefoxDriver().get_driver()
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")
