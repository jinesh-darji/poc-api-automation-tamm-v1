import random

import logging

from utils.api_library import Status
from utils.json_parser import JsonParser


class TestAdmBuah(object):
    """Test cases related to ADNM"""

    def test_to_chk_get_online_user_verification_status(self, api_helper):
        """Test getOnlineUserVerificationStatus: BUAH-1629"""

        national_id = random.randint(14 ** 15, 14 ** 16 - 1)
        resp_code, resp_body, resp_time, resp_header = api_helper. \
            post_response("GetOnlineUserVerificationStatus", "TAMMOwnerProfile", "getOnlineUserVerificationStatus",
                          args=national_id)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response('TAMMOwnerProfile', 'GetOnlineUserVerificationStatus', resp_body), \
            "The response code isn't equal the expected code"

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
        assert JsonParser.validate_response('TAMMOwnerProfile', 'GetOwnerIdByOwnerIDN', resp_body), \
            "The response code isn't equal the expected code"

    def test_get_buy_and_sell_details(self, api_helper):
        """Test GetBuyAndSellDetails: BUAH-3293"""

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

        logging.info('Send request to InitiateService - BuyAndSellUnitService')
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("InitiateService", "IntegratedServices",
                                                                                "getInitiateServiceBuyAndSellUnitService")
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response('IntegratedServices', 'getInitiateService_BuyAndSellUnitService',
                                            resp_body), "The response code isn't equal the expected code"
        application_id_buy_and_sell = JsonParser.get_value_from_dict(resp_body, ['InitiateServiceResponse',
                                                                                 'InitiateServiceResult',
                                                                                 'ApplicationId'])

        logging.info('Send request to CommitService')
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("CommitService", "IntegratedServices",
                                                                                "getCommitService",
                                                                                args=application_id)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response('IntegratedServices', 'getCommitService', resp_body), \
            "The response code isn't equal the expected code"

        logging.info('Send request to CommitService - Buy and Sell')
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("CommitService", "IntegratedServices",
                                                                                "getCommitServiceBuyAndSell",
                                                                                args=application_id_buy_and_sell)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response('IntegratedServices', 'getCommitService_BuyAndSell', resp_body), \
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

    def test_get_property_profile(self, api_helper):
        """Test getPropertyProfile: BUAH-2262"""

        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetPropertyProfile",
                                                                                "TAMMPropertyProfileService",
                                                                                "getPropertyProfile")
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response('TAMMPropertyProfileService', 'getPropertyProfile', resp_body), \
            "The response code isn't equal the expected code"

    # Doesn't work now
    # def test_get_site_plan(self, api_helper):
    #     """Test getSitePlan: """
    #
    #     resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetSitePlan",
    #                                                                             "DigitalData",
    #                                                                             "getSitePlan")
    #     assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
    #     assert JsonParser.validate_response('DigitalData', 'GetSitePlan', resp_body), \
    #         "The response code isn't equal the expected code"

    def test_get_lands_short_list(self, api_helper):
        """Test getLandsShortList: """

        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetLandsShortList",
                                                                                "DigitalData",
                                                                                "getLandsShortList")
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response('DigitalData', 'getLandsShortList', resp_body), \
            "The response code isn't equal the expected code"

    def test_ownership_deed(self, api_helper):
        """Test GetUnitOwnershipDeed: BUAH-2259"""

        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetUnitOwnershipDeed",
                                                                                "TAMMPropertyProfileService",
                                                                                "getUnitOwnershipDeed")
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response('TAMMPropertyProfileService', 'getUnitOwnershipDeed', resp_body), \
            "The response code isn't equal the expected code"

    def test_property_plot_unit(self, api_helper):
        """Test getPropertyPlotUnit: BUAH-3292"""

        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetPropertyPlotUnit",
                                                                                "PropertyPlotUnits",
                                                                                "getPropertyPlotUnit")
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response('PropertyPlotUnits', 'GetPropertyPlotUnit', resp_body), \
            "The response code isn't equal the expected code"

    def test_upload_document(self, api_helper):
        """Test UploadDocument: """

        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("UploadDocument",
                                                                                "IntegratedServices",
                                                                                "getUploadDocument")
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response('IntegratedServices', 'getUploadDocument', resp_body), \
            "The response code isn't equal the expected code"
