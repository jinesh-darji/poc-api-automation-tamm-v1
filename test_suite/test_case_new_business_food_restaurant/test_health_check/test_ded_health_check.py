import os
import logging
import allure
import pytest
from utils.json_parser import JsonParser
from test_suite.test_case_new_business_food_restaurant.conftest import allure_naming
from utils.api_library import Status


@allure.feature('DED')
class TestDedNbfr(object):
    """Test cases related to DED"""

    token = ""

    @pytest.mark.health_check
    def test_authenticate_user(self, api_helper):
        """Test authenticateUser : NBFR-1369"""

        logging.info('Send request to InitiateService')
        headers = api_helper.config_parser().build_headers("core_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("authenticateUser", "DED",
                                                                                "authenticateUser",
                                                                                headers=headers)
        self.token = JsonParser.get_json_value('Result:Token', resp_body)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    @pytest.mark.health_check
    def test_business_license(self, api_helper):
        """Test businessLicense : NBFR-1372"""

        self.test_authenticate_user(api_helper)
        logging.info('Send request to businessLicense')
        headers = api_helper.config_parser().build_headers("core_header")
        params = {"token": self.token}
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("businessLicense", "DED",
                                                                                "businessLicense", params,
                                                                                headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    @pytest.mark.health_check
    def test_business_amendment(self, api_helper):
        """Test businessAmendment : NBFR-1373"""

        self.test_authenticate_user(api_helper)
        logging.info('Send request to businessAmendment')
        headers = api_helper.config_parser().build_headers("core_header")
        params = {"token": self.token}
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("businessAmendment", "DED",
                                                                                "businessAmendment",
                                                                                params, headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    @pytest.mark.health_check
    def test_check_application_status(self, api_helper):
        """Test checkApplicationStatus : NBFR-1374"""

        self.test_authenticate_user(api_helper)
        logging.info('Send request to checkApplicationStatus')
        headers = api_helper.config_parser().build_headers("core_header")
        params = {"token": self.token}
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("checkApplicationStatus",
                                                                                'DED',
                                                                                'checkApplicationStatus',
                                                                                params, headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    @pytest.mark.health_check
    def test_trade_name_check(self, api_helper):
        """Test tradeNameCheck : NBFR-1370"""

        self.test_authenticate_user(api_helper)
        logging.info('Send request to tradeNameCheck')
        headers = api_helper.config_parser().build_headers("core_header")
        params = {"token": self.token}
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("tradeNameCheck", 'DED',
                                                                                'tradeNameCheck',
                                                                                params, headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    @pytest.mark.health_check
    def test_business_name(self, api_helper):
        """Test businessName : NBFR-1371"""

        self.test_authenticate_user(api_helper)
        logging.info('Send request to businessName')
        headers = api_helper.config_parser().build_headers("core_header")
        params = {"token": self.token}
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("businessName", 'DED',
                                                                                'businessName',
                                                                                params, headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    @pytest.mark.health_check
    def test_upload_document(self, api_helper):
        """Test uploadDocument : NBFR-1376"""

        self.test_authenticate_user(api_helper)
        logging.info('Send request to uploadDocument')
        headers = api_helper.config_parser().build_headers("core_header")
        files = {'file': open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "resources", "sample.pdf"),
                              'rb')}
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response_file_upload("uploadDocument",
                                                                                            files, headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    @pytest.mark.health_check
    def test_business_certificate(self, api_helper):
        """Test businessCertificate : NBFR-1375"""

        self.test_authenticate_user(api_helper)
        logging.info('Send request to businessCertificate')
        headers = api_helper.config_parser().build_headers("core_header")
        params = {"token": self.token}
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("businessCertificate", 'DED',
                                                                                'businessCertificate',
                                                                                params, headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    @pytest.mark.health_check
    def test_check_linked_license(self, api_helper):
        """Test checkLinkedLicense : NBFR-1377"""

        self.test_authenticate_user(api_helper)
        logging.info('Send request to checkLinkedLicense')
        headers = api_helper.config_parser().build_headers("core_header")
        params = {"token": self.token}
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("checkLinkedLicense", 'DED',
                                                                                'checkLinkedLicense',
                                                                                params, headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    @pytest.mark.health_check
    def test_get_fees(self, api_helper):
        """Test getFees : NBFR-1378"""

        logging.info('Send request to getFees')
        headers = api_helper.config_parser().build_headers("core_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("getFees", 'DED', 'getFees',
                                                                                headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    @pytest.mark.health_check
    def test_list_trade_licenses(self, api_helper):
        """Test listTradeLicenses : NBFR-1379"""

        logging.info('Send request to listTradeLicenses')
        headers = api_helper.config_parser().build_headers("core_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("listTradeLicenses", 'DED',
                                                                                'listTradeLicenses', headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    @pytest.mark.health_check
    def test_get_trade_license_details(self, api_helper):
        """Test getTradeLicenseDetails : NBFR-1380"""

        logging.info('Send request to getTradeLicenseDetails')
        headers = api_helper.config_parser().build_headers("core_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("getTradeLicenseDetails", 'DED',
                                                                                'getTradeLicenseDetails',
                                                                                headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
