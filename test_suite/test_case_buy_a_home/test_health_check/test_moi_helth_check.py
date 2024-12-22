import allure
import pytest

from utils.api_library import Status


@allure.feature('MOI')
class TestMoiBuah(object):
    """Test cases related to MOI"""

    @pytest.mark.health_check
    def test_get_person_profile(self, api_helper):
        """Test getPersonProfile: "BUAH-2673"""

        headers = api_helper.config_parser().build_headers("microservices_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetPersonProfile",
                                                                                "DigitalData",
                                                                                "getPersonProfile", headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    @pytest.mark.health_check
    def test_get_site_plan(self, api_helper):
        """Test getSitePlan: """

        headers = api_helper.config_parser().build_headers("microservices_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetSitePlan",
                                                                                "DigitalData",
                                                                                "getSitePlan", headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    @pytest.mark.health_check
    def test_get_family_book_details(self, api_helper):
        """Test getFamilyBookDetails: BUAH-2675"""

        headers = api_helper.config_parser().build_headers("microservices_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetFamilyBookDetails",
                                                                                "DigitalData",
                                                                                "getFamilyBookDetails", headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"
