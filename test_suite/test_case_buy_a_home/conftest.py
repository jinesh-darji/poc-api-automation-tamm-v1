import re
from _operator import contains

import pytest
from hamcrest import has_property, equal_to, assert_that

from test_data_configuration.test_data_config_parser import Config_parser
from test_suite.test_case_buy_a_home import config
from utils.api_helper import ApiHelper
from allure import MASTER_HELPER as ALLURE_HELPER

from utils.api_library import ApiMethods

@pytest.fixture(scope="session")
def api_helper():
    config_parser = Config_parser(config.APPLICATION_NAME, config.ENVIRONMENT_TYPE, config.PROTOCOL)
    yield ApiHelper(config_parser)

@pytest.fixture(scope='function', autouse=True)
def allure_naming():
    """Using name of method as name of test in allure-report"""
    if ALLURE_HELPER._allurelistener:
        method_name = re.search("\.(?:.(?!\.))+$", str(ALLURE_HELPER._allurelistener.test.name)).group(0).\
            replace('.', '')
        ALLURE_HELPER._allurelistener.test.name = method_name
#
# @pytest.fixture(scope='function', autouse=True)
# @pytest.mark.parametrize('package', ['pytest.allure', 'allure'])
# def test_descriptions(report_for, package):
#     if ALLURE_HELPER._allurelistener:
#         report = report_for("""
#         import pytest
#         import allure
#         def test_x():
#             %s.description('Description')
#         """ % package)
#
#         assert_that(report.findall('.//test-case'),
#                     contains(has_property('description', equal_to('Description'))))
#         method_name = re.search("\.(?:.(?!\.))+$", str(ALLURE_HELPER._allurelistener.test.name)).group(0).\
#             replace('.', '')
#         ALLURE_HELPER._allurelistener.test.name = method_name