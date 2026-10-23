import requests
from utils.config.api_config import BASE_URL,DEFAULT_HEADERS
from api.api_auth import AuthAPI
from api.api_users import UsersAPI
from api.api_products import ProductsAPI

class ClientAPI:
    def __init__(self):
        self.base_url = BASE_URL
        self.session = requests.Session()
        self.session.headers.update(DEFAULT_HEADERS)
        self.auth = AuthAPI(self.session,self.base_url)
        self.users = UsersAPI(self.session,self.base_url)
        self.products = ProductsAPI(self.session,self.base_url)