import logging
from utils.json_parser import JsonParser
from utils.api_library import Status


class TestIcaNbfr(object):
    """Test cases related to ICA"""

    def test_get_person_profile_unified_number(self, api_helper):
        """Test getPersonProfileUnifiedNumber : NBFR-1388"""

        logging.info('Send request to getPersonProfileUnifiedNumber')
        headers = api_helper.config_parser().build_headers("core_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("getPersonProfileUnifiedNumber", 'ICA',
                                                                                'getPersonProfileUnifiedNumber',
                                                                                headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response("ICA", "getPersonProfileUnifiedNumber", resp_body), \
            "The response code isn't equal the expected code"

    def test_get_person_profile_identitiy_card(self, api_helper):
        """Test getPersonProfileIdentityCard : NBFR-1389"""

        logging.info('Send request to getPersonProfileIdentitiyCard')
        headers = api_helper.config_parser().build_headers("core_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("getPersonProfileIdentitiyCard", 'ICA',
                                                                                'getPersonProfileIdentitiyCard',
                                                                                headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response("ICA", "getPersonProfileIdentitiyCard", resp_body), \
            "The response code isn't equal the expected code"
