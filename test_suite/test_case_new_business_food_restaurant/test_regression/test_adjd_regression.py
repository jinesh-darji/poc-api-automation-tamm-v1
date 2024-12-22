import logging
import allure
import pytest
from utils.json_parser import JsonParser
from utils.api_library import Status


class TestAdjdNbfr(object):
    """Test cases related to ADJD"""

    def test_get_partnership_contract(self, api_helper):
        """Test getPartnershipContract : NBFR-1367"""

        logging.info('Send request to getPartnershipContract')
        headers = api_helper.config_parser().build_headers("core_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("getPartnershipContract",
                                                                                'ADJD', 'getPartnershipContract',
                                                                                headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response("ADJD", "getPartnershipContract", resp_body), \
            "The response code isn't equal the expected code"

    def test_get_partnership_contract_details(self, api_helper):
        """Test getPartnershipContractDetails : NBFR-1368"""

        logging.info('Send request to getPartnershipContractDetails')
        headers = api_helper.config_parser().build_headers("core_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("getPartnershipContractDetails",
                                                                                'ADJD', 'getPartnershipContractDetails',
                                                                                headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response("ADJD", "getPartnershipContractDetails", resp_body), \
            "The response code isn't equal the expected code"

    def test_get_partnership_contract_info(self, api_helper):
        """Test getPartnershipContractInfo : NBFR-1366"""

        logging.info('Send request to getPartnershipContractInfo')
        headers = api_helper.config_parser().build_headers("core_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("getPartnershipContractInfo",
                                                                                'ADJD', 'getPartnershipContractInfo',
                                                                                headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response("ADJD", "getPartnershipContractInfo", resp_body), \
            "The response code isn't equal the expected code"
