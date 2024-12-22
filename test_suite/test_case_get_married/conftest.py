import pytest

from test_data_configuration.test_data_config_parser import Config_parser
from test_suite.test_case_get_married import config
from utils.api_helper import ApiHelper


@pytest.fixture(scope="session")
def api_helper():
    config_parser = Config_parser(config.APPLICATION_NAME, config.ENVIRONMENT_TYPE, config.PROTOCOL)
    yield ApiHelper(config_parser)
