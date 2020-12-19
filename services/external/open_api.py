import requests

from os import path
from flask import current_app
from urllib.parse import urlencode
from configparser import ConfigParser

config = ConfigParser()
config.read(path.abspath(path.join(path.abspath(__file__), "../../../config.ini")))


class OpenAPI(object):
    def __init__(self, host: str, path: str, parameters: dict) -> None:
        """
        Setting OPENAPI host, path url, parameters
        :param host: API host URL
        :param path: API path
        :param parameters: request parameter
        """
        self._host = host
        self._path = path
        self._parameters = parameters

    def set_api_key(self) -> bool:
        """
        setting OPEN API service key
        :return: boolean
        """
        try:
            self._parameters["serviceKey"] = config["OPEN_API"]["SERVICE_KEY"]
            return True

        except Exception as e:
            current_app.logger.error(e)
            return False

    def request(self) -> bool or object:
        """
        request with setting host, path, parameteres
        :return: bool or object
        """
        try:
            self.set_api_key()
            req = requests.get(url=self._host + self._path + "?" + urlencode(query=self._parameters, safe="%"))

            if req is None:
                return None

            resp = req.json()
            return resp

        except Exception as e:
            current_app.logger.error(e)
            return False
