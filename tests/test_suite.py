import json
import requests
import allure

from src.py_project_framework.pageobjects.bookspage import BooksPage
from src.py_project_framework.pageobjects.homepage import HomePage
from src.py_project_framework.pageobjects.profilepage import ProfilePage
from src.py_project_framework.utils.api_constants import ApiConstants
from src.py_project_framework.utils.test_data_util import generate_username


@allure.feature("User Management")
@allure.story("User Login")
@allure.severity(allure.severity_level.CRITICAL)
def test_login(driver_instance, api_session):
    with allure.step("Generate testdata"):
        username = generate_username()
        req_body = {'userName': username, 'password': 'Password@123'}
    with allure.step("Create user via API"):
        api_session.set_headers(ApiConstants.json_content_type_header)
        res = api_session.response(
            api_session.create_user_api_request(req_body))
        assert res.status_code == requests.codes.created
        res_dict = json.loads(res.text)
        assert res_dict.get('username') == username
        assert res_dict.get('books') == []

    with allure.step("Login via UI"):
        home_page = HomePage(driver_instance)
        home_page.open_page()
        home_page.login(username, 'Password@123')
        profile_page = ProfilePage(driver_instance)
        assert profile_page.get_displayed_username() == username


@allure.feature("Book Management")
@allure.story("Book Details Verification")
@allure.severity(allure.severity_level.NORMAL)
def test_book_details(driver_instance, api_session):
    with allure.step("Get books via API"):
        res = api_session.response(api_session.get_books_api_request())
        assert res.status_code == requests.codes.ok
        my_dict = json.loads(res.text)
        api_books_details = []
        for i in my_dict['books']:
            my_books = {'title': i['title'], 'author': i['author'], 'publisher': i['publisher']}
            api_books_details.append(my_books)

    with allure.step("Get books via UI"):
        books_page = BooksPage(driver_instance)
        books_page.open_books_page()
        ui_books_details = books_page.get_all_books_details()

    with allure.step("Compare API and UI book details"):
        assert api_books_details == ui_books_details
