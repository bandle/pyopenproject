import requests
from requests.auth import HTTPBasicAuth

from pyopenproject.api_connection.request import Request


class PatchRequest(Request):

    def __init__(self, connection, context, json=None, headers=None):
        super().__init__(connection=connection, headers=headers, context=context, json=json)

    def _execute_request(self):
        if not self.connection.use_oauth:
            with requests.Session() as s:
                s.auth = HTTPBasicAuth(self.connection.api_user, self.connection.api_key)
                s.headers.update({"Content-Type": "application/json"})
                response = s.patch(self.connection.url_base + self.context, json=self.json)
            return response
        else:
            if not hasattr(self.connection, 'oauth'):
                self.connection.authenticate()
            response = self.connection.oauth.patch(self.connection.url_base + self.context,
                                                   json=self.json,
                                                   headers={"Content-Type": "application/json"})
            return response
