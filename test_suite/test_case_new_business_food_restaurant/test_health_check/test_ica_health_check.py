import logging
import allure
import pytest

from test_suite.test_case_new_business_food_restaurant.conftest import allure_naming
from utils.api_library import Status


@allure.feature('ICA')
class TestIcaNbfr(object):
    """Test cases related to ICA"""

    @pytest.mark.health_check
    def test_get_person_profile_unified_number(self, api_helper):
        """Test getPersonProfileUnifiedNumber : NBFR-1388"""

        logging.info('Send request to getPersonProfileUnifiedNumber')
        headers = api_helper.config_parser().build_headers("core_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("getPersonProfileUnifiedNumber", 'ICA',
                                                                                'getPersonProfileUnifiedNumber',
                                                                                headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    @pytest.mark.health_check
    def test_get_person_profile_identity_card(self, api_helper):
        """Test getPersonProfileIdentityCard : NBFR-1389"""

        logging.info('Send request to getPersonProfileIdentityCard')
        headers = api_helper.config_parser().build_headers("core_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("getPersonProfileIdentitiyCard", 'ICA',
                                                                                'getPersonProfileIdentitiyCard',
                                                                                headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
