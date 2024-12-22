import random

import pytest

from utils.api_library import Status
from utils.json_parser import JsonParser
from utils.validation_util import ValidationUtil


class TestValidationBuah(object):
    """Test cases related to ADDC"""

    def test_get_application_response(self, api_helper):
        """Test GetApplicationResponse: BUAH-3290"""

        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetApplicationResponse",
                                                                                "ADDCNotificationService",
                                                                                "getApplicationResponse")
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response('ADDCNotificationService', 'GetApplicationResponse', resp_body), \
            "The response code isn't equal the expected code"
        ValidationUtil.get_validation_data("getApplicationResponse", resp_body, "buah_validation")

    def test_to_chk_get_owner_id_by_owner_idn(self, api_helper):
        """Test getOwnerIdByOwnerIDN: BUAH-1630"""
        national_id = random.randint(14 ** 15, 14 ** 16 - 1)
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetOwnerIdByOwnerIDN",
                                                                                "TAMMOwnerProfile",
                                                                                "getOwnerIdByOwnerIDN",
                                                                                args=national_id)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        ValidationUtil.get_validation_data("getOwnerIdByOwnerIDN", resp_body, "buah_validation")

    @pytest.mark.parametrize("plot_id", [
        446942])
    def test_getCommitServiceBuyAndSell(self, plot_id, api_helper):

            resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetUnitOwnershipDeed",
                                                                                    "TAMMPropertyProfileService",
                                                                                    "getUnitOwnershipDeedBAv03",
                                                                                    args=plot_id)
            assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
            OwnerId = JsonParser.get_value_from_dict(resp_body, ['GetUnitOwnershipDeedResponse',
                                                                 'GetUnitOwnershipDeedResult',
                                                                 'UnitOwnershipDeed', 'OwnershipDeedShareDetailsList',
                                                                 'OwnershipDeedShareDetails',
                                                                 'OwnerId'])
            RequesterId = OwnerId

            PlotOwnerShareId = JsonParser.get_value_from_dict(resp_body, ['GetUnitOwnershipDeedResponse',
                                                                          'GetUnitOwnershipDeedResult',
                                                                          'UnitOwnershipDeed',
                                                                          'OwnershipDeedShareDetailsList',
                                                                          'OwnershipDeedShareDetails',
                                                                          'PlotOwnerShareId'])

            transaction_amount = 3477600
            IsWithMortgage = "true"
            mortgage_details_issue_date_initiate = "2019-02-20"
            mortgage_details_mortgage_amount_initiate = "5000"
            mortgage_details_AthorizedBankEmployeeId_initiate = "2"
            mortgage_details_MortgageType_initiate = "1"
            mortgage_details_Degree_initiate = "1"
            resp_code, resp_body, resp_time, resp_header = api_helper.post_response("InitiateService",
                                                                                    "IntegratedServices",
                                                                                    "getInitiateServiceBuyAndSellUnitServiceMortgage",
                                                                                    args=(plot_id, transaction_amount,
                                                                                          OwnerId, PlotOwnerShareId,
                                                                                          IsWithMortgage,
                                                                                          mortgage_details_issue_date_initiate,
                                                                                          mortgage_details_mortgage_amount_initiate,
                                                                                          mortgage_details_AthorizedBankEmployeeId_initiate,
                                                                                          mortgage_details_MortgageType_initiate,
                                                                                          mortgage_details_Degree_initiate,
                                                                                          RequesterId))
            assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
            application_id_buy_and_sell = JsonParser.get_value_from_dict(resp_body, ['InitiateServiceResponse',
                                                                                     'InitiateServiceResult',
                                                                                     'ApplicationId'])

            resp_code, resp_body, resp_time, resp_header = api_helper.post_response("CommitService",
                                                                                    "IntegratedServices",
                                                                                    "getCommitServiceBuyAndSell",
                                                                                    args=application_id_buy_and_sell)

            assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
            ValidationUtil.get_validation_data("getCommitServiceBuyAndSell", resp_body, "buah_validation", 0, 1)