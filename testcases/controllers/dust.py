import unittest
import requests

from utils.constants import RESPONSE_CODE


class DustControllerTest(unittest.TestCase):
    def setUp(self) -> None:
        self._host = "http://localhost:5000/dust"
        self._parameter = {
            "region": "seoul"
        }

    def test_get_method_parameter(self):
        req = requests.get(url=self._host,
                           data=self._parameter,
                           headers={'Content-Type': 'application/json'})
        resp = req.json()

        self.assertEqual(resp, RESPONSE_CODE["SUCCESS"])

    def test_get_method_wrong_path(self):
        req = requests.get(url=self._host + "/unknown",
                           headers={'Content-Type': 'application/json'})

        self.assertEqual(req.status_code, 400)