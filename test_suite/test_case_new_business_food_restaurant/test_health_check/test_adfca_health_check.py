import allure
import pytest
import logging

from test_suite.test_case_new_business_food_restaurant.conftest import allure_naming
from utils.api_library import Status


@allure.feature('ADFCA')
class TestAdfcaNbfr(object):
    """Test cases related to ADFCA"""

    @pytest.mark.health_check
    def test_start_noc_process(self, api_helper):
        """Test startNocProcess : NBFR-1360"""

        logging.info('Send request to startNocProcess')
        headers = api_helper.config_parser().build_headers("core_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("startNocProcess", "ADFCA",
                                                                                "startNocProcess",
                                                                                headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    @pytest.mark.health_check
    def test_get_noc_status(self, api_helper):
        """Test getNocStatus : NBFR-1361"""

        logging.info('Send request to getNocStatus')
        headers = api_helper.config_parser().build_headers("core_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("getNocStatus", 'ADFCA',
                                                                                'getNocStatus', headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    @pytest.mark.health_check
    def test_get_inspection_details(self, api_helper):
        """Test getInspectionDetails : NBFR-1362"""

        logging.info('Send request to getInspectionDetails')
        headers = api_helper.config_parser().build_headers("core_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("getInspectionDetails", 'ADFCA',
                                                                                'getInspectionDetails', headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    @pytest.mark.health_check
    def test_submit_payment_details(self, api_helper):
        """Test submitPaymentDetails : NBFR-1363"""

        logging.info('Send request to submitPaymentDetails')
        headers = api_helper.config_parser().build_headers("core_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("submitPaymentDetails", 'ADFCA',
                                                                                'submitPaymentDetails', headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    @pytest.mark.health_check
    def test_get_payment_details(self, api_helper):
        """Test getPaymentDetails : NBFR-1364"""

        logging.info('Send request to getPaymentDetails')
        headers = api_helper.config_parser().build_headers("core_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("getPaymentDetails", 'ADFCA',
                                                                                'getPaymentDetails', headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    @pytest.mark.health_check
    def test_get_certificate(self, api_helper):
        """Test getCertificate : NBFR-1365"""

        logging.info('Send request to getCertificate')
        headers = api_helper.config_parser().build_headers("core_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("getCertificate", 'ADFCA',
                                                                                'getCertificate', headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
