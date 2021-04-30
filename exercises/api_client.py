import requests
import logging

class ApiClient(requests.Session):
    def __init__(self):
        super().__init__()
        self.hooks['response'].append(self._log_details)

    @staticmethod
    def _log_details(response, *args, **kwargs):        
        logging.info(f"{response.request.method}: {response.request.url}")
        logging.info(f"request headers: {response.request.headers}")
        if response.request.body is not None:
            logging.info(f"request body: {response.request.body}")

        logging.info(f"response status: {response.status_code}, elapsed: {response.elapsed.total_seconds()}s")
        logging.info(f"response headers: {response.headers}")
        if response.text != "":
            logging.info(f"response body: {response.text}")