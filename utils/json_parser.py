import json
import os


class JsonParser:

    def dict_to_json(self):
        """
        This method will be used to generate json string from Dict
        :return: dictionary in json formatted string
        """
        json_output = json.dumps(self)
        return json_output

    @staticmethod
    def read_json_file_to_dict(file_location, file_name):
        """
        This method will be used to read Json file in dictionary format
        :param file_location: Location till parent folder
        :param file_name: file name (without .json in name)
        :return: dict type of json data
        """
        with open(file_location + '/' + file_name + '.json') as f:
            data = json.load(f)
        return data

    @staticmethod
    def read_json_file_to_dict_for_validation(file_location, folder_validation, file_name):
        """
        This method will be used to read Json file in dictionary format
        :param folder_validation: name of folder with validation file
        :param file_location: Location till parent folder
        :param file_name: file name (without .json in name)
        :return: dict type of json data
        """
        with open(file_location + '/' + folder_validation + '/' + file_name + '.json') as f:
            data = json.load(f)
        return data

    @staticmethod
    def read_json_file_to_string(file_location, file_name):
        """
        This method will be used to read json file in string format
        :param file_location: Location till parent folder
        :param file_name: file name (without .json in name)
        :return: json string
        """
        with open(file_location + '/' + file_name + '.json') as f:
            data = json.load(f)
        return str(data)

    @staticmethod
    def read_json_file(file_location, file_name):
        """
        This method will be used to read json file in string format
        :param file_location: Location till parent folder
        :param file_name: file name (without .json in name)
        :return: json string
        """
        with open(file_location + '/' + file_name + '.json') as f:
            data = json.load(f)
        return data

    @staticmethod
    def get_value_from_dict(data, keys):
        """
        Get value from dictionary
        :param data: response body
        :param keys: key from JSON
        :return: str: value from JSON according keys
        """
        for key in keys:
            data = data[key]
        return data

    @staticmethod
    def create_payload_for_service(service_name, operation_name, scenario='main'):
        """
        This method will be used to read json from template folder
        :param service_name: Service name
        :param operation_name: Operation name
        :param scenario: (optional) scenario name if a service has more than one type of request
        :return: json payload in string format
        """
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'template/requests'))
        payload = JsonParser.read_json_file_to_dict(file_path, '/' + service_name + '/' + operation_name + '_' +
                                                    scenario)
        # print("payload created  : %s" % payload)
        return json.dumps(payload)

    @staticmethod
    def read_response_template(service_name, operation_name, scenario='response'):
        """
        This method will be used to read json from template folder
        :param operation_name: Operation name
        :param service_name: Service name
        :param scenario: (optional) scenario name if a service has more than one type of request
        :return: json payload in string format
        """
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'template/response'))
        payload = JsonParser.read_json_file(file_path + '/' + service_name, operation_name + '_' + scenario)
        return payload

    @staticmethod
    def get_json_value(key, jsondict):
        """
        This method will be used to get a value from JSON string.
        :param key: Key for the value in following format "parent:child:actualkey"
        :param jsondict: input dict from where value need to be fetched.
        :return:String value at given key.
        """
        keylist = key.split(':')
        temp_json = jsondict

        if len(keylist) == 1:
            return temp_json[key]
        else:
            for key in keylist[:-1]:
                temp_json = temp_json[key]
        return temp_json[keylist[-1]]

    @staticmethod
    def set_json_value(key, value, json_dict):
        """
        This method will be used to set or change a value at given key in Json string.
        :param key: Key for the value in following format "parent:child:actualkey"
        :param value: Value to be updated at given key
        :param json_dict: input dict from where value need to be fetched.
        :return: updated json string with value
        """
        keylist = key.split(':')
        temp_json = json_dict[keylist[0]]

        if len(keylist) == 1:
            json_dict[key] = value

        else:
            key_item = keylist.pop(0)
            json_dict = JsonParser.set_json_value(key_item, JsonParser.set_json_value(":".join(keylist), value,
                                                                                      temp_json), json_dict)
            print("Json :: ")
            print(json_dict)
        return json_dict

    @staticmethod
    def recursive_items(dictionary):
        """
        Recursive list runner
        :param dictionary: dict
        """
        for key, value in dictionary.items():
            if type(value) is dict:
                yield (key)
                yield from JsonParser.recursive_items(value)
            else:
                yield (key)

    @staticmethod
    def validate_response(service_name, operation_name, actual_response):
        """
        Validate response: compare response with etalon JSON
        :param service_name: Services name: folder with response
        :param operation_name: operation name (service name)
        :param actual_response: actual response (resp body)
        :return: bool: True or False
        """
        expected = JsonParser.read_response_template(service_name, operation_name, 'response')

        a = []
        b = []
        for key in JsonParser.recursive_items(expected):
            a.append(key)

        for key in JsonParser.recursive_items(actual_response):
            b.append(key)

        if len(a) == len(b):
            for i in range(len(a)):
                if a[i] != b[i]:
                    return False
        else:
            return False, expected
        return True, expected
