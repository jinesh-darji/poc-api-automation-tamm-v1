import os
import logging
import allure
import pytest

from test_suite.test_case_new_business_food_restaurant.conftest import allure_naming
from utils.api_library import Status


@allure.feature('Docs-converter')
class TestDocConverterNbfr(object):
    """Test cases related to Docs-converter"""

    @pytest.mark.health_check
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
