class BaseAPI:
    def __init__(self, session,base_url):
        self.session = session
        self.base_url = base_url

    def _request(self,method,endpoint,payload=None,params=None):
        return self.session.request(
            method,
            self.base_url + endpoint,
            json=payload,
            params=params)

    def GET(self,endpoint,params=None):
        return self._request('GET',endpoint,params=params)

    def POST(self, endpoint, payload=None):
        return self._request('POST', endpoint,payload=payload)

    def PUT(self, endpoint,payload=None, params=None):
        return self._request('PUT', endpoint,payload=payload, params=params)

    def PATCH(self,endpoint,payload=None, params=None):
        return self._request('PATCH', endpoint,payload=payload,params=params)

    def DELETE(self, endpoint, params=None):
        return self._request('DELETE', endpoint,params=params)

