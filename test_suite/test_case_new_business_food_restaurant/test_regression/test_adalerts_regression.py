import logging
import pytest
from utils.json_parser import JsonParser
from utils.api_library import Status


class TestADAlertsNbfr(object):
    """Test cases related to ADAlerts"""

    def test_email_send_by_address(self, api_helper):
        """Test emailSendByAddress : NBFR-1391"""

        logging.info('Send request to emailSendByAddress')
        headers = api_helper.config_parser().build_headers("core_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("emailSendByAddress", 'ADAlerts',
                                                                                'emailSendByAddress',
                                                                                headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response("ADAlerts", "emailSendByAddress", resp_body), \
            "The response code isn't equal the expected code"

    def test_email_send_by_address_with_attachment(self, api_helper):
        """Test emailSendByAddressWithAttachment : NBFR-1392"""

        logging.info('Send request to emailSendByAddressWithAttachment')
        headers = api_helper.config_parser().build_headers("core_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("emailSendByAddressWithAttachment",
                                                                                'ADAlerts',
                                                                                'emailSendByAddressWithAttachment',
                                                                                headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response("ADAlerts", "emailSendByAddressWithAttachment", resp_body), \
            "The response code isn't equal the expected code"
