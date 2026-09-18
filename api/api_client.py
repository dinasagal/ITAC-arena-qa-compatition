import requests


class ApiClient:

    def __init__(self, base_url, headers=None, timeout=10):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.timeout = timeout

        if headers:
            self.session.headers.update(headers)

    def _build_url(self, endpoint):
        return f"{self.base_url}/{endpoint.lstrip('/')}"

    def get(self, endpoint, **kwargs):
        return self.session.get(
            self._build_url(endpoint),
            timeout=kwargs.pop("timeout", self.timeout),
            **kwargs,
        )

    def post(self, endpoint, **kwargs):
        return self.session.post(
            self._build_url(endpoint),
            timeout=kwargs.pop("timeout", self.timeout),    
            **kwargs,
        )

    def put(self, endpoint, **kwargs):
        return self.session.put(
            self._build_url(endpoint),
            timeout=kwargs.pop("timeout", self.timeout),
            **kwargs,
        )

    def patch(self, endpoint, **kwargs):
        return self.session.patch(
            self._build_url(endpoint),
            timeout=kwargs.pop("timeout", self.timeout),
            **kwargs,
        )

    def delete(self, endpoint, **kwargs):
        return self.session.delete(
            self._build_url(endpoint),
            timeout=kwargs.pop("timeout", self.timeout),
            **kwargs,
        )