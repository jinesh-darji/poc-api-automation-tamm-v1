import logging
import allure
import pytest

from test_suite.test_case_new_business_food_restaurant.conftest import allure_naming
from utils.api_library import Status


@allure.feature('ADAlerts')
class TestADAlertsNbfr(object):
    """Test cases related to ADAlerts"""

    @pytest.mark.health_check
    def test_email_send_by_address(self, api_helper):
        """Test emailSendByAddress : NBFR-1391"""

        logging.info('Send request to emailSendByAddress')
        headers = api_helper.config_parser().build_headers("core_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("emailSendByAddress", 'ADAlerts',
                                                                                'emailSendByAddress',
                                                                                headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    @pytest.mark.health_check
    def test_email_send_by_address_with_attachment(self, api_helper):
        """Test emailSendByAddressWithAttachment : NBFR-1392"""

        logging.info('Send request to emailSendByAddressWithAttachment')
        headers = api_helper.config_parser().build_headers("core_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("emailSendByAddressWithAttachment",
                                                                                'ADAlerts',
                                                                                'emailSendByAddressWithAttachment',
                                                                                headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
