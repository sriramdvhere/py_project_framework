from selenium.webdriver.common.by import By
from selenium import webdriver

from src.py_project_framework.config import Config
from src.py_project_framework.pageobjects.basepage import BasePage


class HomePage(BasePage):
    user_name_id = (By.ID, 'userName')
    password_id = (By.ID, 'password')
    login_btn_id = (By.ID, 'login')

    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.log = super().logger(logger_name=__name__)

    def open_page(self):
        self._driver.get(Config.LOGIN_URL)
        self._driver.set_page_load_timeout(Config.PAGE_LOAD_TIMEOUT)

    def login(self, user_name, password):
        self.log.info(f'Login started for username:{user_name}.')
        self.sendkeys_to_element(HomePage.user_name_id, user_name)
        self.sendkeys_to_element(HomePage.password_id, password)
        self.log.debug("Entered username and password")
        self.click_element(HomePage.login_btn_id)
