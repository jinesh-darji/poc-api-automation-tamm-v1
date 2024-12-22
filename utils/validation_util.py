from test_data_configuration.test_data_config_parser import Config_parser
from test_suite.test_case_buy_a_home import config
from utils.soft_assert import SoftAssert
from utils.json_parser import JsonParser


class ValidationUtil:

    @staticmethod
    def get_validation_data(method, resp_body, name_of_file, *arg):
        global validation_data, validation_path, received_value, validation_list
        config_parser = Config_parser(config.APPLICATION_NAME, config.ENVIRONMENT_TYPE, config.PROTOCOL)
        result = []
        for item in config_parser.get_data_validation_file("Validation:" + method, name_of_file):
            validation_path = JsonParser.get_json_value("path_node", item)
            validation_data = JsonParser.get_json_value("validation_value", item)
            validation_path_list = []
            for i in validation_path.split(','):
                validation_path_list.append(i.replace(' ', ''))
            validation_list = [validation_path_list, validation_data]
            for index_of_arg in range(0, len(arg)):
                value_of_tuple = arg.index(index_of_arg)
                for path_item in validation_list[0]:
                    if path_item == str(value_of_tuple):
                        validation_list[0][validation_list[0].index(str(value_of_tuple))] = value_of_tuple
            received_value = JsonParser.get_value_from_dict(resp_body, validation_list[0])
            if validation_list[1] != received_value:
                result.append([validation_list[1], received_value, validation_path_list])
                SoftAssert.soft_assert(len(result) == 0,
                                       "\n\nValidation for '" + method + "' method in path " + str(validation_list[0]) +
                                       " is failed. Following issue is found: The expected result = "
                                       + str(validation_list[1]) + " , The received result = " + str(received_value))
        SoftAssert.final_assert()
