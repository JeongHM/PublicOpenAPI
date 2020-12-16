import json
import unittest

from utils.constants import RESPONSE_CODE
from utils.decorators import formatting_response


class DecoratorsTest(unittest.TestCase):
    def setUp(self) -> None:
        self._success_status_code = 200
        self._fail_status_code = 400
        self._success_response = RESPONSE_CODE["SUCCESS"]
        self._fail_response = RESPONSE_CODE["FAIL"]

    def test_formatting_response(self):
        @formatting_response
        def success_response():
            return self._success_response, None, self._success_status_code

        response_obj = success_response().__dict__
        response_status_code = response_obj.get("_status_code")
        response_body = json.loads(s=response_obj.get("response")[0])

        self.assertEqual(self._success_status_code, response_status_code)
        self.assertEqual(self._success_response, response_body)

        @formatting_response
        def fail_response():
            return self._fail_response, None, self._fail_status_code

        response_obj = fail_response().__dict__
        response_status_code = response_obj.get("_status_code")
        response_body = json.loads(s=response_obj.get("response")[0])

        self.assertEqual(self._fail_status_code, response_status_code)
        self.assertEqual(self._fail_response, response_body)
