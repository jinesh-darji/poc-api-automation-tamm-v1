import random

import logging

import allure
import pytest

from test_suite.test_case_buy_a_home.conftest import allure_naming
from utils.api_library import Status
from utils.json_parser import JsonParser

@allure.feature('ADM')
class TestAdmBuah(object):
    """Test cases related to test_ADM"""

    @pytest.mark.health_check
    def test_getOnlineUserVerificationStatus(self, api_helper):
        """Test getOnlineUserVerificationStatus: BUAH-1629"""

        national_id = random.randint(14 ** 15, 14 ** 16 - 1)
        headers = api_helper.config_parser().build_headers("microservices_header")
        resp_code, resp_body, resp_time, resp_header = api_helper. \
            post_response("GetOnlineUserVerificationStatus", "TAMMOwnerProfile", "getOnlineUserVerificationStatus",
                          headers=headers, args=national_id)
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

    @pytest.mark.health_check
    def test_to_chk_get_owner_id_by_owner_idn(self, api_helper):
        """Test getOwnerIdByOwnerIDN: BUAH-1630"""
        national_id = random.randint(14 ** 15, 14 ** 16 - 1)
        headers = api_helper.config_parser().build_headers("microservices_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetOwnerIdByOwnerIDN",
                                                                                "TAMMOwnerProfile",
                                                                                "getOwnerIdByOwnerIDN",
                                                                                headers=headers, args=national_id)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    @pytest.mark.health_check
    def test_get_buy_and_sell_details(self, api_helper):
        """Test GetBuyAndSellDetails: BUAH-3293"""

        headers = api_helper.config_parser().build_headers("microservices_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetBuyAndSellDetails",
                                                                                "TAMMOwnerProfile",
                                                                                "getBuyAndSellDetails", headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    @pytest.mark.health_check
    def test_get_lookup_items(self, api_helper):
        """Test GetLookupItems: BUAH-2261"""

        headers = api_helper.config_parser().build_headers("microservices_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetLookupItems",
                                                                                "TAMMOwnerProfile",
                                                                                "getLookupItems", headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    @pytest.mark.health_check
    def test_verification_process(self, api_helper):
        """Test InitiateService, CommitService, GetServiceDetails, getOwnerIdByOwnerIDN: BUAH-1822"""

        logging.info('Send request to InitiateService')
        national_id = random.randint(14 ** 15, 14 ** 16 - 1)
        headers = api_helper.config_parser().build_headers("microservices_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("InitiateService", "IntegratedServices",
                                                                                "getInitiateService",
                                                                                headers=headers, args=national_id)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        application_id = JsonParser.get_value_from_dict(resp_body, ['data', 'applicationId'])

        logging.info('Send request to InitiateService - BuyAndSellUnitService')
        headers = api_helper.config_parser().build_headers("microservices_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("InitiateService", "IntegratedServices",
                                                                                "getInitiateServiceBuyAndSellUnitService",
                                                                                headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        application_id_buy_and_sell = JsonParser.get_value_from_dict(resp_body, ['data', 'applicationId'])

        logging.info('Send request to CommitService')
        headers = api_helper.config_parser().build_headers("microservices_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("CommitService", "IntegratedServices",
                                                                                "getCommitService",
                                                                                headers=headers,
                                                                                args=application_id)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

        logging.info('Send request to CommitService - Buy and Sell')
        headers = api_helper.config_parser().build_headers("microservices_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("CommitService", "IntegratedServices",
                                                                                "getCommitServiceBuyAndSell",
                                                                                headers=headers,
                                                                                args=application_id_buy_and_sell)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

        logging.info('Send request to GetServiceDetails')
        headers = api_helper.config_parser().build_headers("microservices_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetServiceDetails",
                                                                                "IntegratedServices",
                                                                                "getServiceDetails",
                                                                                headers=headers,
                                                                                args=application_id)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

        logging.info('Send request to GetOnlineUserVerificationStatus')
        headers = api_helper.config_parser().build_headers("microservices_header")
        resp_code, resp_body, resp_time, resp_header = api_helper. \
            post_response("GetOnlineUserVerificationStatus", "TAMMOwnerProfile", "getOnlineUserVerificationStatus",
                          headers=headers, args=application_id)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    @pytest.mark.health_check
    def test_get_property_profile(self, api_helper):
        """Test getPropertyProfile: BUAH-2262"""

        headers = api_helper.config_parser().build_headers("microservices_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetPropertyProfile",
                                                                                "TAMMPropertyProfileService",
                                                                                "getPropertyProfile", headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    # Doesn't work now
    # def test_get_site_plan(self, api_helper):
    #     """Test getSitePlan: """
    #
    #     resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetSitePlan",
    #                                                                             "DigitalData",
    #                                                                             "getSitePlan")
    #     assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    # @pytest.mark.health_check
    # def test_get_lands_short_list(self, api_helper):
    #     """Test getLandsShortList: BUAH-3677"""
    #
    #     headers = api_helper.config_parser().build_headers("microservices_header")
    #     resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetLandsShortList",
    #                                                                             "DigitalData",
    #                                                                             "getLandsShortList", headers=headers)
    #     assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    @pytest.mark.health_check
    def test_ownership_deed(self, api_helper):
        """Test GetUnitOwnershipDeed: BUAH-2259"""

        headers = api_helper.config_parser().build_headers("microservices_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetUnitOwnershipDeed",
                                                                                "TAMMPropertyProfileService",
                                                                                "getUnitOwnershipDeed", headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    @pytest.mark.health_check
    def test_property_plot_unit(self, api_helper):
        """Test getPropertyPlotUnit: BUAH-3292"""

        headers = api_helper.config_parser().build_headers("microservices_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetPropertyPlotUnit",
                                                                                "PropertyPlotUnits",
                                                                                "getPropertyPlotUnit", headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    @pytest.mark.health_check
    def test_upload_document(self, api_helper):
        """Test UploadDocument: BUAH-TEST"""

        headers = api_helper.config_parser().build_headers("microservices_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("UploadDocument",
                                                                                "IntegratedServices",
                                                                                "uploadDocument", headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
