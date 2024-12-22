from new_business_food_restaurant_load import config
from test_data_configuration.test_data_config_parser import Config_parser
from utils.load_test_helper import LoadTestHelper

load_test_helper = LoadTestHelper(Config_parser(config.APPLICATION_NAME, config.ENVIRONMENT_TYPE, config.PROTOCOL))
