import random

from utils.api_library import Status
from utils.json_parser import JsonParser


class TestFabBuah(object):
    """Test cases related to FAB"""

    def test_creat_lead_fab(self, api_helper):
        """Test CreateLeadFAB: """

        mobile_number = random.randint(8 ** 9, 9 ** 10)
        email_id = random.randint(8 ** 9, 9 ** 10)
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("CreateLeadFAB", "FAB_Bank",
                                                                                "createLeadFAB",
                                                                                args=(mobile_number, email_id))
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response('FAB_Bank', 'createLeadFAB', resp_body), \
            "The response code isn't equal the expected code"
