import allure
import pytest

from test_data_configuration.test_data_config_parser import Config_parser
from utils.api_library import Status


@allure.feature('ADDC')
class TestAddcBuah(object):
    """Test cases related to ADDC"""

    # @pytest.mark.health_check
    # def test_get_water_electricity_bill_list(self, api_helper):
    #     """Test GetWaterElectricityBillList: BUAH-3289"""
    #     config_parser = Config_parser("buy_a_home", "stg", "protocol_https")
    #     headers = config_parser.build_headers("accept_language_headers")
    #
    #     resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetWaterElectricityBillList",
    #                                                                             "DigitalData",
    #                                                                             "getWaterElectricityBillList",
    #                                                                             headers=headers)
    #     assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    @pytest.mark.health_check
    def test_get_application_response(self, api_helper):
        """Test GetApplicationResponse: BUAH-3290"""

        headers = api_helper.config_parser().build_headers("microservices_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetApplicationResponse",
                                                                                "ADDCNotificationService",
                                                                                "getApplicationResponse",
                                                                                headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"