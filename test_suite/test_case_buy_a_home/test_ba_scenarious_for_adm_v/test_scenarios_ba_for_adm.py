import logging
import sys

import allure
import pytest

from utils.api_library import Status
from utils.json_parser import JsonParser


class TestAdmBuahBA(object):
    """Test cases related to test_ADM BA scenario v.0.3"""

    @pytest.mark.parametrize("plot_id", [
        446942])
    def test_cscenario_1_adm(self, plot_id, api_helper):
        """Test InitiateService, CommitService, GetServiceDetails, getOwnerIdByOwnerIDN: BUAH-1822"""

        with allure.step("Working with \"Deed GetUnitOwnershipDeed\" request"):
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

        with allure.step("Working with \"InitiateService\" request"):
            logging.info('Send request to InitiateService - BuyAndSellUnitService - mortgage')
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

        with allure.step("Working with \"CommitService\" request"):
            logging.info('Send request to CommitService - Buy and Sell')
            resp_code, resp_body, resp_time, resp_header = api_helper.post_response("CommitService",
                                                                                    "IntegratedServices",
                                                                                    "getCommitServiceBuyAndSell",
                                                                                    args=application_id_buy_and_sell)
            if resp_code == Status.SERVER_ERROR:
                list_with_data_error = JsonParser.get_value_from_dict(resp_body, ['Faults', 'BusinessMessageDetails'])
                description_of_error = JsonParser.get_value_from_dict(list_with_data_error[0], ['Description'])
                print("\n" + description_of_error)
                sys.exit(0)

            assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

            aplication_number_commit_service = JsonParser.get_value_from_dict(resp_body, ['CommitServiceResult',
                                                                                          'ApplicationData',
                                                                                          'ApplicationNumber'])

            status = JsonParser.get_value_from_dict(resp_body, ['CommitServiceResult',
                                                                'ApplicationData',
                                                                'Status'])

            assert status == "Awaiting Payment", "Statuses from commit Service requests are not equal"

            payment_data_list = JsonParser.get_value_from_dict(resp_body, ['CommitServiceResult',
                                                                           'ApplicationData',
                                                                           'PaymentsInfo', 'PaymentData'])

            customer_name_buyer = JsonParser.get_value_from_dict(payment_data_list[0], ['CustomerName'])
            customer_name_seller = JsonParser.get_value_from_dict(payment_data_list[1], ['CustomerName'])

            total_fee_amount_buyer = JsonParser.get_value_from_dict(payment_data_list[0], ['TotalFeeAmount'])
            assert total_fee_amount_buyer == transaction_amount * 0.01, \
                "Amount from InitiateService isn't equal amount from CommitService"

            fee_const_buyer = payment_data_list[0]['FeeLineItems']['FeelineItem'][0]['FeeConst']
            assert fee_const_buyer == "BuyAndSellUnitBuyer", "Fee consts are not equal"

            total_fee_amount_seller = JsonParser.get_value_from_dict(payment_data_list[1], ['TotalFeeAmount'])

            assert total_fee_amount_seller == transaction_amount * 0.01, \
                "Amount from InitiateService isn't equal amount from CommitService"

            fee_const_seller = payment_data_list[1]['FeeLineItems']['FeelineItem'][0]['FeeConst']
            assert fee_const_seller == "BuyAndSellUnitSeller", "Fee consts are not equal"


            application_create_date = JsonParser.get_value_from_dict(resp_body, ['CommitServiceResult',
                                                                                 'ApplicationData',
                                                                                 'ApplicationCreateDate'])

        with allure.step("Working with \"GetServiceDetails\" request"):
            logging.info('Send request to GetServiceDetails')
            resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetServiceDetails",
                                                                                    "IntegratedServices",
                                                                                    "getServiceDetailsBA",
                                                                                    args=application_id_buy_and_sell)

            assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

            aplication_number_fet_service_details = JsonParser.get_value_from_dict(resp_body,
                                                                                   ['GetServiceDetailsResult',
                                                                                    'ApplicationData',
                                                                                    'ApplicationNumber'])
            assert aplication_number_fet_service_details == aplication_number_commit_service, \
                "app numbers for commit and ger service details are not equal"

            status_get_service_details = JsonParser.get_value_from_dict(resp_body, ['GetServiceDetailsResult',
                                                                                    'ApplicationData',
                                                                                    'Status'])
            assert status_get_service_details == "Awaiting Payment", \
                "Statuses from getServiceDetails requests are not equal"

            eLMSStatus_get_service_details = JsonParser.get_value_from_dict(resp_body, ['GetServiceDetailsResult',
                                                                                        'ApplicationData',
                                                                                        'eLMSStatus'])
            assert eLMSStatus_get_service_details == "Fee Payment", \
                "eLMSStatus from getServiceDetails requests are not equal"

            isWithMortgage_get_service_details = JsonParser.get_value_from_dict(resp_body, ['GetServiceDetailsResult',
                                                                                            'ApplicationData',
                                                                                            'ApplicationDataExtension',
                                                                                            'IsWithMortgage'])
            # assert isWithMortgage_get_service_details == "true", \
            #     "IsWithMortgage from getServiceDetails requests is not equal IsWithMortgage from Initiate"

            mortgage_details_issue_date_get_service_details = JsonParser.get_value_from_dict(resp_body,
                                                                                             ['GetServiceDetailsResult',
                                                                                              'ApplicationData',
                                                                                              'ApplicationDataExtension',
                                                                                              'MortgageDetails',
                                                                                              'IssueDate'])
            assert mortgage_details_issue_date_get_service_details == mortgage_details_issue_date_initiate, \
                "MortgageDetails.IssueDate from getServiceDetails is not equal IssueDate from Initiate"

            mortgage_details_mortgage_amount_get_service_details = JsonParser.get_value_from_dict(resp_body,
                                                                                                  [
                                                                                                      'GetServiceDetailsResult',
                                                                                                      'ApplicationData',
                                                                                                      'ApplicationDataExtension',
                                                                                                      'MortgageDetails',
                                                                                                      'MortgageAmount'])
            assert mortgage_details_mortgage_amount_get_service_details == mortgage_details_mortgage_amount_initiate, \
                "MortgageDetails.MortgageAmount from getServiceDetails are not equal"

            mortgage_details_AthorizedBankEmployeeId_get_service_details = JsonParser.get_value_from_dict(resp_body,
                                                                                      ['GetServiceDetailsResult',
                                                                                          'ApplicationData',
                                                                                          'ApplicationDataExtension',
                                                                                          'MortgageDetails',
                                                                                          'AuthorizedBankEmployeeId'])
            assert mortgage_details_AthorizedBankEmployeeId_get_service_details == \
                   mortgage_details_AthorizedBankEmployeeId_initiate, \
                "MortgageDetails.AuthorizedBankEmployeeId from getServiceDetails are not equal"

            mortgage_details_MortgageType_get_service_details = JsonParser.get_value_from_dict(resp_body,
                                                                                       ['GetServiceDetailsResult',
                                                                                           'ApplicationData',
                                                                                           'ApplicationDataExtension',
                                                                                           'MortgageDetails',
                                                                                           'MortgageType'])
            assert mortgage_details_MortgageType_get_service_details == \
                   mortgage_details_MortgageType_initiate, \
                "MortgageDetails.MortgageType from getServiceDetails are not equal"

            mortgage_details_Degree_get_service_details = JsonParser.get_value_from_dict(resp_body,
                                                                                         ['GetServiceDetailsResult',
                                                                                          'ApplicationData',
                                                                                          'ApplicationDataExtension',
                                                                                          'MortgageDetails',
                                                                                          'Degree'])
            assert mortgage_details_Degree_get_service_details == \
                   mortgage_details_Degree_initiate, \
                "MortgageDetails.Degree from getServiceDetails are not equal"
