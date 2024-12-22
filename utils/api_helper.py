from utils import json_parser
from utils.api_library import ApiMethods
from utils.json_parser import JsonParser

"""Class for all api methods used in test script """


class ApiHelper(object):

    def __init__(self, config_parser):
        self.__config_parser = config_parser
        self.__libclient = ApiMethods(self.__config_parser.main_url())
        self.__default_headers = {}

    def post_response(self, endpoint, api, resp_path, headers=None, parameters=None, files=None, args=None):
        """
        Post response
        :param endpoint: end-point link for request
        :param api: name of folder with request
        :param resp_path: path with response
        :param headers: header of request
        :param parameters: parameters
        :param files: files
        :param args: additional parameters if need to add parameter in JSON file
        :return: str: response code and additional information
        """
        if headers:
            headers = headers
        else:
            self.__default_headers = self.__config_parser.build_headers("core_header")
            headers = self.__default_headers
        #self.__config_parser.build_headers("core_header")
        #headers = headers if headers else self.__default_headers
        end_point = self.__config_parser.endpoint_parser(endpoint)
        json_parser_method = JsonParser()
        if isinstance(args, list):
            args = tuple(args)
        if args and not isinstance(args, tuple):
            args = (args,)
        if args is None:
            body = json_parser_method.create_payload_for_service(api, resp_path)
        else:
            body = json_parser_method.create_payload_for_service(api, resp_path) % args
        return self.__libclient.put_response_data(end_point, body, headers, parameters, files)

    def get_response(self, endpoint, headers=None, params=None):
        """
        Get response
        :param endpoint: end-point link for request
        :param headers: header
        :param params: parameters
        :return: str: response code and additional information
        """
        headers = headers if headers else self.__default_headers
        end_point = self.__config_parser.endpoint_parser(endpoint)
        return self.__libclient.get_response_data(end_point, headers, params)

    def post_response_file_upload(self, endpoint, headers=None, files=None):
        """
        Post response with file uploaded
        :param endpoint: end-point link for request
        :param headers: header
        :param files: file data
        :return: str: response code and additional information
        """
        headers = headers if headers else self.__default_headers
        end_point = self.__config_parser.endpoint_parser(endpoint)
        return self.__libclient.put_response_data(end_point, None, headers, files)

    def config_parser(self):
        return self.__config_parser