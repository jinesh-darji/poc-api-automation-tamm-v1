import os
from utils.api_library import Status
from test_data_configuration.test_data_config_parser import Config_parser

"""In the following test cases only the response code will be checked for the services"""


class TestVADTHealthCheck(object):

    def test_visa_countries_response(self, api_helper):
        resp_code, resp_body, resp_time, resp_header = api_helper.get_response("visa_app_countries")
        assert resp_code == Status.SUCCESS, "Visa countries response is not 200"

    def test_visa_emirates_response(self, api_helper):
        resp_code, resp_body, resp_time, resp_header = api_helper.get_response("visa_app_emirates")
        assert resp_code == Status.SUCCESS, "Emirates response code is not 200"

    def test_visa_ports_response(self, api_helper):
        resp_code, resp_body, resp_time, resp_header = api_helper.get_response("visa_app_ports")
        assert resp_code == Status.SUCCESS, "Ports code response is not 200"

    def test_visa_dial_codes_response(self, api_helper):
        resp_code, resp_body, resp_time, resp_header = api_helper.get_response("visa_app_dial_codes")
        assert resp_code == Status.SUCCESS, "Dial Codes response is not 200"

    def test_visa_scan_passport_response(self, api_helper):
        config_parser = Config_parser("visit_abu_dhabi", "test", "protocol_https")
        headers = config_parser.build_headers("upload_file_headers")
        files = {'file': open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "resources", "passport.jpg"),
                              'rb')}
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response_file_upload("visa_app_scan_passport",
                                                                                            headers, files)
        assert resp_code == Status.SUCCESS, "Passport Scan response is not 200"

    def test_visa_nationality_check(self, api_helper):
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("visa_app_residency_check", "Visa",
                                                                                "Residency")
        assert resp_code == Status.SUCCESS, "Nationality Check response code is not 200"

    def test_visa_residency_check(self, api_helper):
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("visa_app_nationality_check", "Visa",
                                                                                "nationality")
        assert resp_code == Status.SUCCESS, "Residency Check response is not 200"

    def test_visa_options_check(self, api_helper):
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("visa_app_options", "Visa", "options")
        assert resp_code == Status.SUCCESS, "Visa Options response code is not 200"

    def test_manage_visa_token(self, api_helper):
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("visa_app_options", "Visa", "token")
        assert resp_code == Status.SUCCESS, "Visa token response code is not 200"
