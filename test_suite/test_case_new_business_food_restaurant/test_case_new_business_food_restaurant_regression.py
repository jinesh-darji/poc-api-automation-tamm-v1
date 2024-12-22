import logging
import os
from utils.json_parser import JsonParser
from utils.api_library import Status


class TestCaseNbfrRegression(object):

    """Test cases related to ADFCA"""

    def test_start_noc_process(self, api_helper):
        """Test startNocProcess : NBFR-1360"""

        logging.info('Send request to startNocProcess')
        headers = api_helper.config_parser().build_headers("core_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("startNocProcess", "ADFCA",
                                                                                "startNocProcess",
                                                                                headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response("ADFCA", "startNocProcess", resp_body), \
            "The response code isn't equal the expected code"

    def test_get_noc_status(self, api_helper):
        """Test getNocStatus : NBFR-1361"""

        logging.info('Send request to getNocStatus')
        headers = api_helper.config_parser().build_headers("core_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("getNocStatus", 'ADFCA',
                                                                                'getNocStatus', headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response("ADFCA", "getNocStatus", resp_body), \
            "The response code isn't equal the expected code"

    def test_get_inspection_details(self, api_helper):
        """Test getInspectionDetails : NBFR-1362"""

        logging.info('Send request to getInspectionDetails')
        headers = api_helper.config_parser().build_headers("core_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("getInspectionDetails", 'ADFCA',
                                                                                'getInspectionDetails', headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response("ADFCA", "getInspectionDetails", resp_body), \
            "The response code isn't equal the expected code"

    def test_submit_payment_details(self, api_helper):
        """Test submitPaymentDetails : NBFR-1363"""

        logging.info('Send request to submitPaymentDetails')
        headers = api_helper.config_parser().build_headers("core_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("submitPaymentDetails", 'ADFCA',
                                                                                'submitPaymentDetails', headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response("ADFCA", "submitPaymentDetails", resp_body), \
            "The response code isn't equal the expected code"

    def test_get_payment_details(self, api_helper):
        """Test getPaymentDetails : NBFR-1364"""

        logging.info('Send request to getPaymentDetails')
        headers = api_helper.config_parser().build_headers("core_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("getPaymentDetails", 'ADFCA',
                                                                                'getPaymentDetails', headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response("ADFCA", "getPaymentDetails", resp_body), \
            "The response code isn't equal the expected code"

    def test_get_certificate(self, api_helper):
        """Test getCertificate : NBFR-1365"""

        logging.info('Send request to getCertificate')
        headers = api_helper.config_parser().build_headers("core_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("getCertificate", 'ADFCA',
                                                                                'getCertificate', headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response("ADFCA", "getCertificate", resp_body), \
            "The response code isn't equal the expected code"

    """Test cases related to ADJD"""

    def test_get_partnership_contract(self, api_helper):
        """Test getPartnershipContract : NBFR-1367"""

        logging.info('Send request to getPartnershipContract')
        headers = api_helper.config_parser().build_headers("core_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("getPartnershipContract",
                                                                                'ADJD', 'getPartnershipContract',
                                                                                headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response("ADJD", "getPartnershipContract", resp_body), \
            "The response code isn't equal the expected code"

    def test_get_partnership_contract_details(self, api_helper):
        """Test getPartnershipContractDetails : NBFR-1368"""

        logging.info('Send request to getPartnershipContractDetails')
        headers = api_helper.config_parser().build_headers("core_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("getPartnershipContractDetails",
                                                                                'ADJD', 'getPartnershipContractDetails',
                                                                                headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response("ADJD", "getPartnershipContractDetails", resp_body), \
            "The response code isn't equal the expected code"

    def test_get_partnership_contract_info(self, api_helper):
        """Test getPartnershipContractInfo : NBFR-1366"""

        logging.info('Send request to getPartnershipContractInfo')
        headers = api_helper.config_parser().build_headers("core_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("getPartnershipContractInfo",
                                                                                'ADJD', 'getPartnershipContractInfo',
                                                                                headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response("ADJD", "getPartnershipContractInfo", resp_body), \
            "The response code isn't equal the expected code"

    """Test cases related to DED"""

    token = ""

    def test_authenticate_user(self, api_helper):
        """Test authenticateUser : NBFR-1369"""

        logging.info('Send request to InitiateService')
        headers = api_helper.config_parser().build_headers("core_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("authenticateUser", "DED",
                                                                                "authenticateUser",
                                                                                headers=headers)
        self.token = JsonParser.get_json_value('Result:Token', resp_body)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response("DED", "authenticateUser", resp_body), \
            "The response code isn't equal the expected code"

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
        assert JsonParser.validate_response("DED", "businessLicense", resp_body), \
            "The response code isn't equal the expected code"

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
        assert JsonParser.validate_response("DED", "businessAmendment", resp_body), \
            "The response code isn't equal the expected code"

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
        assert JsonParser.validate_response("DED", "checkApplicationStatus", resp_body), \
            "The response code isn't equal the expected code"

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
        assert JsonParser.validate_response("DED", "tradeNameCheck", resp_body), \
            "The response code isn't equal the expected code"

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
        assert JsonParser.validate_response("DED", "businessName", resp_body), \
            "The response code isn't equal the expected code"

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
        assert JsonParser.validate_response("DED", "uploadDocument", resp_body), \
            "The response code isn't equal the expected code"

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
        assert JsonParser.validate_response("DED", "businessCertificate", resp_body), \
            "The response code isn't equal the expected code"

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
        assert JsonParser.validate_response("DED", "checkLinkedLicense", resp_body), \
            "The response code isn't equal the expected code"

    def test_get_fees(self, api_helper):
        """Test getFees : NBFR-1378"""

        logging.info('Send request to getFees')
        headers = api_helper.config_parser().build_headers("core_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("getFees", 'DED', 'getFees',
                                                                                headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response("DED", "getFees", resp_body), \
            "The response code isn't equal the expected code"

    def test_list_trade_licenses(self, api_helper):
        """Test listTradeLicenses : NBFR-1379"""

        logging.info('Send request to listTradeLicenses')
        headers = api_helper.config_parser().build_headers("core_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("listTradeLicenses", 'DED',
                                                                                'listTradeLicenses', headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response("DED", "listTradeLicenses", resp_body), \
            "The response code isn't equal the expected code"

    def test_get_trade_license_details(self, api_helper):
        """Test getTradeLicenseDetails : NBFR-1380"""

        logging.info('Send request to getTradeLicenseDetails')
        headers = api_helper.config_parser().build_headers("core_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("getTradeLicenseDetails", 'DED',
                                                                                'getTradeLicenseDetails',
                                                                                headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response("DED", "getTradeLicenseDetails", resp_body), \
            "The response code isn't equal the expected code"

    """Test cases related to ADM"""

    token_adm = ""

    def test_authenticate_user_adm(self, api_helper):
        """Test getToken : NBFR-1381"""

        logging.info('Send request to InitiateService')
        headers = api_helper.config_parser().build_headers("core_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("getToken", "ADM", "getToken",
                                                                                headers=headers)
        self.token_adm = JsonParser.get_json_value('Result:Token', resp_body)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response("ADM", "getToken", resp_body), \
            "The response code isn't equal the expected code"

    def test_business_license_adm(self, api_helper):
        """Test getListOfConsultantsAndContractors : NBFR-1382"""

        self.test_authenticate_user(api_helper)
        logging.info('Send request to businessLicense')
        headers = api_helper.config_parser().build_headers("core_header")
        params = {"token": self.token_adm}
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("businessLicense", "ADM",
                                                                                "businessLicense", params,
                                                                                headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response("ADM", "businessLicense", resp_body), \
            "The response code isn't equal the expected code"

    """Test cases related to DOH"""

    def test_get_health_insurance(self, api_helper):
        """Test getHealthInsurance : NBFR-1383"""

        logging.info('Send request to getHealthInsurance')
        headers = api_helper.config_parser().build_headers("core_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("getHealthInsurance", 'DOH',
                                                                                'getHealthInsurance', headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response("DOH", "getHealthInsurance", resp_body), \
            "The response code isn't equal the expected code"

    def test_get_health_insurance_emirates_id(self, api_helper):
        """Test getHealthInsuranceEmiratesID : NBFR-1384"""

        logging.info('Send request to getHealthInsuranceEmiratesID')
        headers = api_helper.config_parser().build_headers("core_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("getHealthInsuranceEmiratesID", 'DOH',
                                                                                'getHealthInsuranceEmiratesID',
                                                                                headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response("DOH", "getHealthInsuranceEmiratesID", resp_body), \
            "The response code isn't equal the expected code"

    def test_get_fitness_certificate(self, api_helper):
        """Test getFitnessCertificate : NBFR-1385"""

        logging.info('Send request to getFitnessCertificate')
        headers = api_helper.config_parser().build_headers("core_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("getFitnessCertificate", 'DOH',
                                                                                'getFitnessCertificate',
                                                                                headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response("DOH", "getFitnessCertificate", resp_body), \
            "The response code isn't equal the expected code"

    """Test cases related to Tawtheeq"""

    def test_get_tawtheeq_details(self, api_helper):
        """Test getTawtheeqDetails : NBFR-1386"""

        logging.info('Send request to getTawtheeqDetails')
        headers = api_helper.config_parser().build_headers("core_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("getTawtheeqDetails", 'Tawtheeq',
                                                                                'getTawtheeqDetails', headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response("Tawtheeq", "getTawtheeqDetails", resp_body), \
            "The response code isn't equal the expected code"

    def test_get_tawtheeq_list(self, api_helper):
        """Test getTawtheeqList : NBFR-1387"""

        logging.info('Send request to getTawtheeqList')
        headers = api_helper.config_parser().build_headers("core_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("getTawtheeqList", 'Tawtheeq',
                                                                                'getTawtheeqList', headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response("Tawtheeq", "getTawtheeqList", resp_body), \
            "The response code isn't equal the expected code"

    """Test cases related to ICA"""

    def test_get_person_profile_unified_number(self, api_helper):
        """Test getPersonProfileUnifiedNumber : NBFR-1388"""

        logging.info('Send request to getPersonProfileUnifiedNumber')
        headers = api_helper.config_parser().build_headers("core_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("getPersonProfileUnifiedNumber", 'ICA',
                                                                                'getPersonProfileUnifiedNumber',
                                                                                headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response("ICA", "getPersonProfileUnifiedNumber", resp_body), \
            "The response code isn't equal the expected code"

    def test_get_person_profile_identitiy_card(self, api_helper):
        """Test getPersonProfileIdentityCard : NBFR-1389"""

        logging.info('Send request to getPersonProfileIdentitiyCard')
        headers = api_helper.config_parser().build_headers("core_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("getPersonProfileIdentitiyCard", 'ICA',
                                                                                'getPersonProfileIdentitiyCard',
                                                                                headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response("ICA", "getPersonProfileIdentitiyCard", resp_body), \
            "The response code isn't equal the expected code"

    """Test cases related to Docs-converter"""

    def test_convert_document(self, api_helper):
        """Test convertDocument : NBFR-1390"""

        self.test_authenticate_user(api_helper)
        logging.info('Send request to convertDocument')
        headers = api_helper.config_parser().build_headers("core_header")
        files = {'file': open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "resources", "sample.pdf"),
                              'rb')}
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response_file_upload("convertDocument",
                                                                                            files, headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response("Docs-converter", "convertDocument", resp_body), \
            "The response code isn't equal the expected code"

    """Test cases related to ADAlerts"""

    def test_email_send_by_address(self, api_helper):
        """Test emailSendByAddress : NBFR-1391"""

        logging.info('Send request to emailSendByAddress')
        headers = api_helper.config_parser().build_headers("core_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("emailSendByAddress", 'ADAlerts',
                                                                                'emailSendByAddress',
                                                                                headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response("ADAlerts", "emailSendByAddress", resp_body), \
            "The response code isn't equal the expected code"

    def test_email_send_by_address_with_attachment(self, api_helper):
        """Test emailSendByAddressWithAttachment : NBFR-1392"""

        logging.info('Send request to emailSendByAddressWithAttachment')
        headers = api_helper.config_parser().build_headers("core_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("emailSendByAddressWithAttachment",
                                                                                'ADAlerts',
                                                                                'emailSendByAddressWithAttachment',
                                                                                headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response("ADAlerts", "emailSendByAddressWithAttachment", resp_body), \
            "The response code isn't equal the expected code"
