import allure
import pytest

from utils.api_library import Status


@allure.feature('ETISALAT')
class TestEtisalatBuah(object):
    """Test cases related to Etisalat"""

    @pytest.mark.health_check
    def test_create_lead(self, api_helper):
        """Test OpCreateLead: BUAH-1870"""

        headers = api_helper.config_parser().build_headers("microservices_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("OpCreateLead",
                                                                                "LeadManagementCUD",
                                                                                "getOpCreateLead", headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    @pytest.mark.health_check
    def test_lead_status_inquiry(self, api_helper):
        """Test OpLeadStatusInquiry: BUAH-1868"""

        headers = api_helper.config_parser().build_headers("microservices_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("OpLeadStatusInquiry",
                                                                                "LeadManagementR",
                                                                                "getOpLeadStatusInquiry",
                                                                                headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    @pytest.mark.health_check
    def test_get_package_details(self, api_helper):
        """Test OpGetPackageDetails: BUAH-2258"""

        headers = api_helper.config_parser().build_headers("microservices_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("OpGetPackageDetails",
                                                                                "LeadManagementR",
                                                                                "opGetPackageDetails", headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
