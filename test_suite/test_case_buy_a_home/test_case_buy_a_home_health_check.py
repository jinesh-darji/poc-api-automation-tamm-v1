import random

import logging

from utils.api_library import Status
from utils.json_parser import JsonParser


class TestCasesBuah(object):
    """Test cases related to Property registration"""

    def test_to_chk_get_online_user_verification_status(self, api_helper):
        """Test getOnlineUserVerificationStatus: BUAH-1629"""

        national_id = random.randint(14 ** 15, 14 ** 16 - 1)
        resp_code, resp_body, resp_time, resp_header = api_helper. \
            post_response("GetOnlineUserVerificationStatus", "TAMMOwnerProfile", "getOnlineUserVerificationStatus",
                          args=national_id)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    # @pytest.mark.parametrize("path_request", [
    #     "getOnlineUserVerificationStatusWrongParam", "getOnlineUserVerificationStatusMissParam"])
    # def test_to_chk_get_online_user_verification_status_failed(self, path_request, api_helper):
    #     """Test getOnlineUserVerificationStatus: Wrong parameters: BUAH-1631, bug - BUAH-1632"""
    #
    #     national_id = random.randint(14 ** 15, 14 ** 16 - 1)
    #     resp_code, resp_body, resp_time, resp_header = api_helper. \
    #         post_response("GetOnlineUserVerificationStatus", "TAMMOwnerProfile", path_request, args=national_id)
    #     assert resp_code == Status.BAD_REQUEST, "The response code isn't equal the expected code"

    def test_to_chk_get_owner_id_by_owner_idn(self, api_helper):
        """Test getOwnerIdByOwnerIDN: BUAH-1630"""
        national_id = random.randint(14 ** 15, 14 ** 16 - 1)
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetOwnerIdByOwnerIDN",
                                                                                "TAMMOwnerProfile",
                                                                                "getOwnerIdByOwnerIDN",
                                                                                args=national_id)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    def test_get_buy_and_sell_details(self, api_helper):
        """Test GetBuyAndSellDetails: """

        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetBuyAndSellDetails",
                                                                                "TAMMOwnerProfile",
                                                                                "getBuyAndSellDetails")
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    def test_get_lookup_items(self, api_helper):
        """Test GetLookupItems: BUAH-2261"""

        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetLookupItems",
                                                                                "TAMMOwnerProfile",
                                                                                "getLookupItems")
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

    def test_create_lead_etisalat(self, api_helper):
        """Test OpCreateLead: BUAH-1870"""

        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("OpCreateLead",
                                                                                "LeadManagementCUD",
                                                                                "getOpCreateLead")
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    def test_verification_process(self, api_helper):
        """Test InitiateService, CommitService, GetServiceDetails, getOwnerIdByOwnerIDN: BUAH-1822"""

        logging.info('Send request to InitiateService')
        national_id = random.randint(14 ** 15, 14 ** 16 - 1)
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("InitiateService", "IntegratedServices",
                                                                                "getInitiateService",
                                                                                args=national_id)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        application_id = JsonParser.get_value_from_dict(resp_body, ['InitiateServiceResponse', 'InitiateServiceResult',
                                                                    'ApplicationId'])

        logging.info('Send request to CommitService')
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("CommitService", "IntegratedServices",
                                                                                "getCommitService",
                                                                                args=application_id)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

        logging.info('Send request to GetServiceDetails')
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetServiceDetails",
                                                                                "IntegratedServices",
                                                                                "getServiceDetails",
                                                                                args=application_id)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

        logging.info('Send request to GetOnlineUserVerificationStatus')
        resp_code, resp_body, resp_time, resp_header = api_helper. \
            post_response("GetOnlineUserVerificationStatus", "TAMMOwnerProfile", "getOnlineUserVerificationStatus",
                          args=application_id)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    def test_ownership_deed(self, api_helper):
        """Test GetUnitOwnershipDeed: BUAH-2259"""

        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetUnitOwnershipDeed",
                                                                                "TAMMPropertyProfileService",
                                                                                "getUnitOwnershipDeed")
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    def test_get_property_profile(self, api_helper):
        """Test getPropertyProfile: BUAH-2262"""

        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetPropertyProfile",
                                                                                "TAMMPropertyProfileService",
                                                                                "getPropertyProfile")
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    def test_get_person_profile(self, api_helper):
        """Test getPersonProfile: "BUAH-2673"""

        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetPersonProfile",
                                                                                "DigitalData",
                                                                                "getPersonProfile")
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    def test_get_lands_short_list(self, api_helper):
        """Test getLandsShortList: BUAH-2674"""

        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetLandsShortList",
                                                                                "DigitalData",
                                                                                "getLandsShortList")
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    def test_property_plot_unit(self, api_helper):
        """Test getPropertyPlotUnit: """

        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetPropertyPlotUnit",
                                                                                "PropertyPlotUnits",
                                                                                "getPropertyPlotUnit")
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    def test_get_site_plan(self, api_helper):
        """Test getSitePlan: """

        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetSitePlan",
                                                                                "DigitalData",
                                                                                "getSitePlan")
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    def test_get_family_book_details(self, api_helper):
        """Test getFamilyBookDetails: BUAH-2675"""

        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetFamilyBookDetails",
                                                                                "DigitalData",
                                                                                "getFamilyBookDetails")
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    def test_add_app(self, api_helper):
        """Test addApp: """

        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("AddApp",
                                                                                "HousingApplicationService",
                                                                                "addApp")
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    def test_search_app_by_emirate_id(self, api_helper):
        """Test searchAppByEmirateId: """

        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("SearchAppByEmirateId",
                                                                                "HousingApplicationService",
                                                                                "searchAppByEmirateId")
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
