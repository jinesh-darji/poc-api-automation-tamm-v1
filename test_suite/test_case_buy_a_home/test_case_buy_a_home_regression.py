import logging
import random

from utils.api_library import Status
from utils.json_parser import JsonParser


class TestCasesBuahRegression(object):
    """Test cases related to Property registration"""

    def test_to_chk_get_online_user_verification_statuss_response(self, api_helper):
        """Test getOnlineUserVerificationStatus: BUAH-1629"""

        national_id = random.randint(14 ** 15, 14 ** 16 - 1)
        resp_code, resp_body, resp_time, resp_header = api_helper. \
            post_response("GetOnlineUserVerificationStatus", "TAMMOwnerProfile", "getOnlineUserVerificationStatus",
                          args=national_id)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response('TAMMOwnerProfile', 'GetOnlineUserVerificationStatus', resp_body), \
            "The response code isn't equal the expected code"

    def test_to_chk_get_owner_id_by_owner_idn_response(self, api_helper):
        """Test getOwnerIdByOwnerIDN: BUAH-1630"""

        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetOwnerIdByOwnerIDN",
                                                                                "TAMMOwnerProfile",
                                                                                "getOwnerIdByOwnerIDN")
        assert resp_code == Status.SUCCESS, "failed"
        assert JsonParser.validate_response('TAMMOwnerProfile', 'GetOwnerIdByOwnerIDN', resp_body), \
            "The response code isn't equal the expected code"

    def test_lead_status_inquiry(self, api_helper):
        """Test OpLeadStatusInquiry: BUAH-1868"""

        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("OpLeadStatusInquiry",
                                                                                "LeadManagementR",
                                                                                "getOpLeadStatusInquiry")
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response('LeadManagementR', 'getOpLeadStatusInquiry', resp_body), \
            "The response code isn't equal the expected code"

    def test_op_get_package_details(self, api_helper):
        """Test OpGetPackageDetails: BUAH-2258"""

        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("OpGetPackageDetails",
                                                                                "LeadManagementR",
                                                                                "opGetPackageDetails")
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response('LeadManagementR', 'opGetPackageDetails', resp_body), \
            "The response code isn't equal the expected code"

    def test_create_lead_etisalat(self, api_helper):
        """Test OpCreateLead: BUAH-1870"""

        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("OpCreateLead",
                                                                                "LeadManagementCUD",
                                                                                "getOpCreateLead")
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response('LeadManagementCUD', 'getOpCreateLead', resp_body), \
            "The response code isn't equal the expected code"

    def test_verification_process(self, api_helper):
        """Test InitiateService, CommitService, GetServiceDetails, getOwnerIdByOwnerIDN: BUAH-1822"""

        logging.info('Send request to InitiateService')
        national_id = random.randint(14 ** 15, 14 ** 16 - 1)
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("InitiateService", "IntegratedServices",
                                                                                "getInitiateService",
                                                                                args=national_id)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response('IntegratedServices', 'getInitiateService', resp_body), \
            "The response code isn't equal the expected code"
        application_id = JsonParser.get_value_from_dict(resp_body, ['InitiateServiceResponse', 'InitiateServiceResult',
                                                                    'ApplicationId'])

        logging.info('Send request to CommitService')
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("CommitService", "IntegratedServices",
                                                                                "getCommitService",
                                                                                args=application_id)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response('IntegratedServices', 'getCommitService', resp_body), \
            "The response code isn't equal the expected code"

        logging.info('Send request to GetServiceDetails')
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetServiceDetails",
                                                                                "IntegratedServices",
                                                                                "getServiceDetails",
                                                                                args=application_id)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response('IntegratedServices', 'getServiceDetails', resp_body), \
            "The response code isn't equal the expected code"

        logging.info('Send request to GetOnlineUserVerificationStatus')
        resp_code, resp_body, resp_time, resp_header = api_helper. \
            post_response("GetOnlineUserVerificationStatus", "TAMMOwnerProfile", "getOnlineUserVerificationStatus",
                          args=application_id)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response('TAMMOwnerProfile', 'getOnlineUserVerificationStatus', resp_body), \
            "The response code isn't equal the expected code"

    def test_ownership_deed(self, api_helper):
        """Test GetUnitOwnershipDeed: BUAH-2259"""

        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetUnitOwnershipDeed",
                                                                                "TAMMPropertyProfileService",
                                                                                "getUnitOwnershipDeed")
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response('TAMMPropertyProfileService', 'getUnitOwnershipDeed', resp_body), \
            "The response code isn't equal the expected code"

    def test_get_buy_and_sell_details(self, api_helper):
        """Test GetBuyAndSellDetails: BUAH-2260"""

        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetBuyAndSellDetails",
                                                                                "TAMMOwnerProfile",
                                                                                "getBuyAndSellDetails")
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response('TAMMOwnerProfile', 'getBuyAndSellDetails', resp_body), \
            "The response code isn't equal the expected code"

    def test_get_lookup_items(self, api_helper):
        """Test GetLookupItems: BUAH-2261"""

        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetLookupItems",
                                                                                "TAMMOwnerProfile",
                                                                                "getLookupItems")
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response('TAMMOwnerProfile', 'getLookupItems', resp_body), \
            "The response code isn't equal the expected code"

    def test_get_property_profile(self, api_helper):
        """Test GetLookupItems: BUAH-2262"""

        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetPropertyProfile",
                                                                                "TAMMPropertyProfileService",
                                                                                "getPropertyProfile")
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response('TAMMPropertyProfileService', 'getPropertyProfile', resp_body), \
            "The response code isn't equal the expected code"

    def test_get_person_profile(self, api_helper):
        """Test getPersonProfile: BUAH-2673"""

        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetPersonProfile",
                                                                                "DigitalData",
                                                                                "getPersonProfile")
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response('DigitalData', 'getPersonProfile', resp_body), \
            "The response code isn't equal the expected code"

    def test_get_lands_short_list(self, api_helper):
        """Test getLandsShortList: BUAH-2674"""

        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetLandsShortList",
                                                                                "DigitalData",
                                                                                "getLandsShortList")
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response('DigitalData', 'getLandsShortList', resp_body), \
            "The response code isn't equal the expected code"

    def test_get_family_book_details(self, api_helper):
        """Test getFamilyBookDetails: BUAH-2675"""

        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetFamilyBookDetails",
                                                                                "DigitalData",
                                                                                "getFamilyBookDetails")
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response('DigitalData', 'getFamilyBookDetails', resp_body), \
            "The response code isn't equal the expected code"
