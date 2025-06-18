from requests import Session, Request, Response
from typing import Dict

from socks import method

from src.py_project_framework.config import Config
from src.py_project_framework.utils.api_constants import ApiConstants
from src.py_project_framework.utils.logger_config import get_logger


class ApiSession:

    def __init__(self):
        self._session = Session()
        self.log = get_logger(logger_name=__name__)

    def get_session(self):
        return self

    def set_headers(self, headers: Dict[str, str]):
        self._session.headers.update(headers)

    def response(self, req: Request) -> Response:
        try:
            res = self._session.send(req.prepare())
            self.log.info(f'response from api: {req.url}, response content:{res.content}')
            return res
        except Exception as e:
            print(e)

    def create_user_api_request(self, req_body):
        self.log.info(f'preparing request to trigger '
                      f'api url: {Config.BASE_URL}{ApiConstants.create_user_api_url}'
                      f' with username:{req_body['userName']}')
        return Request(method=ApiConstants.post,
                       url=f'{Config.BASE_URL}{ApiConstants.create_user_api_url}',
                       json=req_body)

    def get_books_api_request(self):
        self.log.info(f'preparing request to trigger api url: '
                      f'{Config.BASE_URL}{ApiConstants.get_books_api_url}')
        return Request(method=ApiConstants.get,
                       url=f'{Config.BASE_URL}{ApiConstants.get_books_api_url}')

    def close_session(self):
        self._session.close()
