import json
import requests
import time

"""Class for all variables used in test script """


class Status:
    SUCCESS = 200
    BAD_REQUEST = 400
    UNAUTHORISED = 401
    SERVER_ERROR = 500
    MISSING_SOURCE = 404


"""Class for all api methods used in test script"""


class ApiMethods:
    def __init__(self, app_url):
        self.app_url = app_url

    def get_response_data(self, url, headers=None, params=None):
        """
        Get response data
        :param url: URL
        :param headers: header
        :param params: Parameters
        :return: str: resp code
        """
        app_url = self.app_url + url
        start = time.time()
        resp = requests.get(app_url, params=params, headers=headers)
        resp_header = resp.headers
        resp_time = time.time() - start
        try:
            output = json.loads(resp.text)
            return resp.status_code, output, resp_time, resp_header
        except:
            return resp.status_code, None, resp_time, resp_header

    def put_response_data(self, url, body, headers=None, parameters=None, files=None):
        """
        Put response data
        :param url: URL
        :param body: Body data
        :param headers: Headers
        :param parameters: Parameters
        :param files: files data
        :return: resp code
        """
        app_url = self.app_url + url
        start = time.time()
        # print(app_url)
        resp = requests.post(app_url, body, headers=headers, params=parameters, files=files)
        resp_header = resp.headers
        resp_time = time.time() - start
        try:
            output = json.loads(resp.text)
            return resp.status_code, output, resp_time, resp_header
        except:
            return resp.status_code, None, resp_time, resp_header
