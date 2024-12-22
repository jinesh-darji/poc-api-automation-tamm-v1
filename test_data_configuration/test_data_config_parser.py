import configparser
import os
import sys

from utils.json_parser import JsonParser

"""Class with helper functions which will parse the values from test data configuration files"""


class Config_parser(object):
    def __init__(self, journey_name, env, protocol):

        self.journey_name = journey_name
        self.env = env
        self.protocol = protocol
        self.config = configparser.ConfigParser()
        self.path = ""

        if __name__ == '__main__':
            path = os.path.split(sys.argv[0])[0]
        else:
            path = os.path.split(__file__)[0]

        self.path = path

        self.config.read(os.path.join(path, self.journey_name + '_test_data.conf'))

    def get_data_validation_file(self, data_key, name_of_file):
        data = JsonParser.read_json_file_to_dict_for_validation(os.path.dirname(os.path.abspath(__file__)),
                                                                "test_data_validation", name_of_file)
        for key in data_key.split(":"):
            data = data[key]
        return data

    def path_env(self):
        return self.path

    def build_headers(self, headertype):

        global username, api_key, centrasite_apikey, centrasite_for, accept_language, accept_language_sas, user_token, api_key_capital
        try:
            username = self.config.get(self.env, "username")
        except configparser.NoOptionError:
            pass
        try:
            api_key = self.config.get(self.env, "apikey")
        except configparser.NoOptionError:
            pass
        try:
            centrasite_apikey = self.config.get(self.env, "x-CentraSite-APIKey")
        except configparser.NoOptionError:
            pass
        try:
            api_key_capital = self.config.get(self.env, "Api-Key")
        except configparser.NoOptionError:
            pass
        try:
            centrasite_for = self.config.get(self.env, "x-Forwarded-For")
        except configparser.NoOptionError:
            pass

        try:
            accept_language = self.config.get(self.env, "Accept-Language")
        except configparser.NoOptionError:
            print("No accept language headers")
        try:
            accept_language_sas = self.config.get(self.env, "Accept-Language-SAS")
        except configparser.NoOptionError:
            print("No accept language sas headers")
        try:
            user_token = self.config.get(self.env, "UserToken")
        except configparser.NoOptionError:
            print("No accept user token headers")

        if headertype == "headers":
            headers = {
                "Username": username,
                "Content-Type": "application/json",
                "apikey": api_key
            }
        elif headertype == "core_header":
            headers = {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "x-CentraSite-APIKey": centrasite_apikey,
                "x-Forwarded-For": centrasite_for
            }
        elif headertype == "microservices_header":
            headers = {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Api-Key": api_key_capital,
                "x-Forwarded-For": centrasite_for
            }
        elif headertype == "inventoryheaders":
            headers = {
                "Username": username,
                "Content-Type": "application/csv",
                "apikey": api_key
            }
        elif headertype == "emptyheaders":
            headers = {}
        elif headertype == "Invalidheaders":
            headers = {
                "Username": username,
                "Content-Type": "application/pdf",
                "apikey": api_key
            }
        elif headertype == "GetMarriedheaders":
            headers = {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Api-Key": api_key
            }
        elif headertype == "upload_file_headers":
            headers = {
                "x-CentraSite-APIKey": centrasite_apikey
            }
        elif headertype == "upload_file_headers":
            headers = {
                "x-Forwarded-For": centrasite_for
            }
        elif headertype == "accept_language_headers":
            headers = {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "x-CentraSite-APIKey": centrasite_apikey,
                "x-Forwarded-For": centrasite_for,
                "Accept-Language": accept_language
            }
        elif headertype == "accept_language_sas":
            headers = {
                "Content-Type": "application/json",
                "Accept-Language": accept_language_sas,
                "UserToken": user_token
            }
        else:
            headers = {
                "Username": "test_user",
                "Content-Type": "application/json",
                "apikey": "test_api"
            }
        return headers

    def endpoint_parser(self, endpoint_name):
        end_point = self.config.get("url", endpoint_name)
        return end_point

    def main_url(self):
        protocol = self.config.get(self.protocol, "protocol")
        domain = self.config.get(self.env, "domain")
        main_url = protocol + domain
        return main_url
