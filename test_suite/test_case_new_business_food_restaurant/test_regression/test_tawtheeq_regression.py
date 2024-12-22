import logging
from utils.json_parser import JsonParser
from utils.api_library import Status


class TestTawtheeqNbfr(object):

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
