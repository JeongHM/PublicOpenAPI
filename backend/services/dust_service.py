from backend.app import config

class DustService(object):
    def __init__(self, headers, bodies):
        self._headers = headers
        self._body = bodies

    def check_headers(self):
        if not self._headers.get('api-key') or \
                self._headers.get('api-key') != config['KEY']['API_KEY']:
            return False
        return True

    def check_bodies(self):
        if not self._body:
            return False
        return True