from utils.json_parser import JsonParser


class LoadTestHelper(object):
    def __init__(self, config_parser):
        self.__config_parser = config_parser
        self.host = self.__config_parser.main_url()

        self.__default_headers = self.__config_parser.build_headers("core_header")

    def post(self, client, endpoint, api, resp_path, headers=None, parameters=None, files=None, args=None):
        headers = headers if headers else self.__default_headers
        end_point = self.__config_parser.endpoint_parser(endpoint)
        if isinstance(args, list):
            args = tuple(args)
        if args and not isinstance(args, tuple):
            args = (args,)
        if args is None:
            body = JsonParser.create_payload_for_service(api, resp_path)
        else:
            body = JsonParser.create_payload_for_service(api, resp_path) % args
        return client.post(end_point, body, headers=headers, params=parameters, files=files)

    def get(self, client, endpoint, headers=None, params=None):
        headers = headers if headers else self.__default_headers
        end_point = self.__config_parser.endpoint_parser(endpoint)

        return client.get(end_point, headers=headers, params=params)
