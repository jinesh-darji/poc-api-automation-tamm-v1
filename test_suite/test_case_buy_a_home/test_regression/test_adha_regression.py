from utils.api_library import Status
from utils.json_parser import JsonParser


class TestAdhaBuah(object):
    """Test cases related to ADHA"""

    def test_add_app(self, api_helper):
        """Test addApp: """

        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("AddApp",
                                                                                "HousingApplicationService",
                                                                                "addApp")
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response('HousingApplicationService', 'AddApp', resp_body), \
            "The response code isn't equal the expected code"

    def test_search_app_by_emirate_id(self, api_helper):
        """Test searchAppByEmirateId: BUAH-3291"""

        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("SearchAppByEmirateId",
                                                                                "HousingApplicationService",
                                                                                "searchAppByEmirateId")
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response('HousingApplicationService', 'SearchAppByEmirateId', resp_body), \
            "The response code isn't equal the expected code"
