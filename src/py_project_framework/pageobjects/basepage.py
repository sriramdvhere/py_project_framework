from typing import Tuple, List

from selenium.webdriver.support.wait import WebDriverWait

from src.py_project_framework.config import Config
from src.py_project_framework.utils.logger_config import get_logger
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self._driver = driver

    def logger(self, logger_name):
        return get_logger(logger_name)

    def sendkeys_to_element(self, locator: Tuple[str, str], value):
        self._driver.find_element(*locator).send_keys(value)

    def click_element(self, locator: Tuple[str, str]):
        self.get_element_with_wait(locator).click()

    def get_element_with_wait(self, locator: Tuple[str, str]):
        return WebDriverWait(self._driver, Config.EXPLICIT_ELEMENT_WAIT).until(
            EC.presence_of_element_located(locator)
        )

    def get_all_elements(self, locator):
        return self._driver.find_elements(*locator)

    def get_text_of_all_elements(self, lst_of_elements: List):
        return [item.text for item in lst_of_elements]
