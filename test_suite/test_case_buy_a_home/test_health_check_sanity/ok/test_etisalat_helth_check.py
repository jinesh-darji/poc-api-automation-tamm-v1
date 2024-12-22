from utils.api_library import Status


class TestEtisalatBuah(object):
    """Test cases related to Etisalat"""

    def test_create_lead_etisalat(self, api_helper):
        """Test OpCreateLead: BUAH-1870"""

        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("OpCreateLead",
                                                                                "LeadManagementCUD",
                                                                                "getOpCreateLead")
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    def test_lead_status_inquiry(self, api_helper):
        """Test OpLeadStatusInquiry: BUAH-1868"""

        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("OpLeadStatusInquiry",
                                                                                "LeadManagementR",
                                                                                "getOpLeadStatusInquiry")
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    def test_op_get_package_details(self, api_helper):
        """Test OpGetPackageDetails: BUAH-2258"""

        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("OpGetPackageDetails",
                                                                                "LeadManagementR",
                                                                                "opGetPackageDetails")
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
