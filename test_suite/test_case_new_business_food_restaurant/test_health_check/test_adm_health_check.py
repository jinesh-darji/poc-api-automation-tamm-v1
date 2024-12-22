import logging
import allure
import pytest
from utils.json_parser import JsonParser
from test_suite.test_case_new_business_food_restaurant.conftest import allure_naming
from utils.api_library import Status


@allure.feature('ADM')
class TestDedNbfr(object):
    """Test cases related to ADM"""

    token = ""

    @pytest.mark.health_check
    def test_authenticate_user(self, api_helper):
        """Test getToken : NBFR-1381"""

        logging.info('Send request to InitiateService')
        headers = api_helper.config_parser().build_headers("core_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("getToken", "ADM", "getToken",
                                                                                headers=headers)
        self.token = JsonParser.get_json_value('Result:Token', resp_body)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    @pytest.mark.health_check
    def test_business_license(self, api_helper):
        """Test getListOfConsultantsAndContractors : NBFR-1382"""

        self.test_authenticate_user(api_helper)
        logging.info('Send request to businessLicense')
        headers = api_helper.config_parser().build_headers("core_header")
        params = {"token": self.token}
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("businessLicense", "ADM",
                                                                                "businessLicense", params,
                                                                                headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
