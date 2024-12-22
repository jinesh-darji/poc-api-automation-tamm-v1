import logging
import allure
import pytest

from test_suite.test_case_new_business_food_restaurant.conftest import allure_naming
from utils.api_library import Status


@allure.feature('Tawtheeq')
class TestTawtheeqNbfr(object):
    """Test cases related to Tawtheeq"""

    @pytest.mark.health_check
    def test_get_tawtheeq_details(self, api_helper):
        """Test getTawtheeqDetails : NBFR-1386"""

        logging.info('Send request to getTawtheeqDetails')
        headers = api_helper.config_parser().build_headers("core_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("getTawtheeqDetails", 'Tawtheeq',
                                                                                'getTawtheeqDetails', headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    @pytest.mark.health_check
    def test_get_tawtheeq_list(self, api_helper):
        """Test getTawtheeqList : NBFR-1387"""

        logging.info('Send request to getTawtheeqList')
        headers = api_helper.config_parser().build_headers("core_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("getTawtheeqList", 'Tawtheeq',
                                                                                'getTawtheeqList', headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
