from utils.api_library import Status
from utils.json_parser import JsonParser


class TestMoiBuah(object):
    """Test cases related to MOI"""

    def test_get_person_profile(self, api_helper):
        """Test getPersonProfile: "BUAH-2673"""

        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetPersonProfile",
                                                                                "DigitalData",
                                                                                "getPersonProfile")
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response('DigitalData', 'getPersonProfile', resp_body), \
            "The response code isn't equal the expected code"

    def test_get_family_book_details(self, api_helper):
        """Test getFamilyBookDetails: BUAH-2675"""

        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetFamilyBookDetails",
                                                                                "DigitalData",
                                                                                "getFamilyBookDetails")
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
        assert JsonParser.validate_response('DigitalData', 'getFamilyBookDetails', resp_body), \
            "The response code isn't equal the expected code"
