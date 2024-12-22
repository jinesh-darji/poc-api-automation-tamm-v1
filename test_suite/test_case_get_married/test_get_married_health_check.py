import pytest

from test_data_configuration.test_data_config_parser import Config_parser
from utils.api_library import Status
from utils.json_parser import JsonParser

"""In the following test cases only the response code will be checked for the services"""


class TestCasesGetMarried(object):

    @pytest.mark.health_check
    def test_pmmc_appointment_response(self, api_helper):
        """
        parameter in get_response method is the name of your endpoint in template.conf file
        """

        config_parser = Config_parser("get_married","test","protocol_https")
        headers = config_parser.build_headers("GetMarriedheaders")

        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("availableappointmentsByAppType",
                                                                        "GM_PMMC", "availableappointmentsByAppType",headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response("GM_PMMC", "availableappointmentsByAppType", resp_body), "failed"

    @pytest.mark.health_check
    def test_book_mazzon_response(self, api_helper):
        """
        parameter in get_response method is the name of your endpoint in template.conf file
        """

        config_parser = Config_parser("get_married","test","protocol_https")
        headers = config_parser.build_headers("GetMarriedheaders")

        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("getBookMazzon",
                                                                        "GM_BookMazzon", "getBookMazzon",headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response("GM_BookMazzon", "getBookMazzon", resp_body), "failed"

