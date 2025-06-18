from selenium import webdriver
from selenium.webdriver.common.by import By

from src.py_project_framework.pageobjects.basepage import BasePage


class ProfilePage(BasePage):
    username_locator = (By.ID, 'userName-value')

    def __init__(self, driver: webdriver):
        super().__init__(driver)
        self.log = super().logger(logger_name=__name__)


    def get_displayed_username(self):
        username = self.get_element_with_wait(ProfilePage.username_locator).text
        self.log.info(f'Logged in username:{username}')
        return username
