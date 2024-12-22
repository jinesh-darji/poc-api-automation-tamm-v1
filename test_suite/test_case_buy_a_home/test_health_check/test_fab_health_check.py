import random

import allure
import pytest

from test_data_configuration.test_data_config_parser import Config_parser
from utils.api_library import Status


@allure.feature('FAB')
class TestFabBuah(object):
    """Test cases related to FAB"""

    @pytest.mark.health_check
    def test_creat_lead_fab(self, api_helper):
        """Test CreateLeadFAB: BUAH-3678"""

        mobile_number = random.randint(8 ** 9, 9 ** 10)
        email_id = random.randint(8 ** 9, 9 ** 10)
        headers = api_helper.config_parser().build_headers("microservices_header")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("CreateLeadFAB", "FAB_Bank",
                                                                                "createLeadFAB", headers=headers,
                                                                                args=(mobile_number, email_id))

        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"