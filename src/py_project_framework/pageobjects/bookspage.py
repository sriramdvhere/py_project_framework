from selenium.webdriver.common.by import By

from src.py_project_framework.config import Config
from src.py_project_framework.pageobjects.basepage import BasePage


class BooksPage(BasePage):
    title_locator = (By.XPATH, "//*[contains(@class,'rt-td')]//a")
    author_locator = (By.XPATH, "//*[contains(@class,'rt-tr-group')]//div[@class='rt-td'][3]")
    publisher_locator = (By.XPATH, "//*[contains(@class,'rt-tr-group')]//div[@class='rt-td'][4]")

    def __init__(self, driver):
        super().__init__(driver)
        self.log = super().logger(logger_name=__name__)

    def open_books_page(self):
        self._driver.get(Config.BOOKS_URL)
        self._driver.set_page_load_timeout(Config.PAGE_LOAD_TIMEOUT)

    def get_all_books_details(self):
        title_of_all_books = self.get_text_of_all_elements(
            self.get_all_elements(BooksPage.title_locator))
        author_of_all_books = self.get_text_of_all_elements(
            self.get_all_elements(BooksPage.author_locator))
        publisher_of_all_books = self.get_text_of_all_elements(
            self.get_all_elements(BooksPage.publisher_locator))
        book_details_dict = []
        for i in range(len(title_of_all_books)):
            book_detail = {'title': title_of_all_books[i], 'author': author_of_all_books[i],
                           'publisher': publisher_of_all_books[i]}
            book_details_dict.append(book_detail)
        return book_details_dict
