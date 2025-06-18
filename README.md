# py_project_framework
## Overview
Python automation framework for both Web and API Testing. It uses pytest for test execution and Allure for reporting.
 

**Tech stack used:**
- python 3.13
- poetry
- pytest
- selenium
- requests
- allure-pytest
- pytest-html

## Project Structure
```
src/
    py_project_framework/
        pageobjects/
            bookspage.py
            homepage.py
            profilepage.py
        utils/
            api_constants.py
            test_data_util.py
tests/
    test_login.py
    test_book_details.py
```
## Key Components
- `pageobjects/`: Contains Page Object Model classes for UI interactions
- `utils/`: Utility modules for API constants and test data generation
- `tests/`: Test files containing test functions

## Dependencies
- python 3.13
- poetry
- pytest
- selenium
- requests
- allure-pytest
- pytest-html

## Running Tests
1. Run tests with Allure:
```pytest --alluredir=./allure-results```
2. Generate and view the Allure report:
```allure serve ./allure-results```
