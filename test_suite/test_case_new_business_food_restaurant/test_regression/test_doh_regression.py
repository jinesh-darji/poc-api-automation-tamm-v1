import logging
from utils.json_parser import JsonParser
from utils.api_library import Status


class TestDohNbfr(object):
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

    def test_get_health_insurance_emitares_id(self, api_helper):
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
