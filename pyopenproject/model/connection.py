import json
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

class Connection:
    """
    Class Configuration,
    represents the connection realized with the web application
    """
    def __init__(self, url, apikey=None, user=None, client_id=None, client_secret=None):
        """Constructor for class Connection
        :param url: The application url
        :param apikey: The apikey
        :param user: The user (optional)
        """
        self.url_base = url
        self.use_oauth = False if apikey else True
        if apikey:
            self.api_user = "apikey" if user is None else user
            self.api_key = apikey
        else:
            self.client_id = client_id
            self.client_secret = client_secret

    def authenticate(self):
        client = BackendApplicationClient(client_id=self.client_id)
        self.oauth = OAuth2Session(client=client)
        self.token = self.oauth.fetch_token(token_url=self.url_base+'/oauth/token', client_id=self.client_id,
                                  client_secret=self.client_secret)

    def __str__(self):
        """
        Returns the object as a string JSON

        :return: JSON as a string
        """
        return json.dumps(self.__dict__)
