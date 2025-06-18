import pytest

from src.py_project_framework.config import Config
from src.py_project_framework.driverfactory import DriverFactory
from src.py_project_framework.utils.api_util import ApiSession


@pytest.fixture(scope='function')
def driver_instance():
    driver = DriverFactory().get_driver(browser_name=Config.BROWSER)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def api_session():
    yield ApiSession().get_session()
    ApiSession().close_session()
