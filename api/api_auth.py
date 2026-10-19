from api.api_base import BaseAPI

class AuthAPI(BaseAPI):

    def _set_token(self, token):
        self.session.headers.update({'Authorization':
                                         f"Bearer {token}"})

    def login(self, payload):
        response = self.POST("/auth/login", payload)
        if response.status_code == 200:
            self._set_token(response.json()['accessToken'])
        return response

    def current_user(self,):
        return self.GET("/auth/me")

    def refresh_token(self,payload):
        response = self.POST("/auth/refresh", payload)
        if response.status_code == 200:
            self._set_token(response.json()['accessToken'])
        return response

    def logout(self):
        return self.session.headers.pop("Authorization", None)