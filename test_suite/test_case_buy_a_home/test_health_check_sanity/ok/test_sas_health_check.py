from utils.api_library import Status


class TestSasBuah(object):
    """Test cases related to SAS"""

    def test_check_coverage(self, api_helper):
        """Test checkCoverage: BUAH-3665"""
        headers = api_helper.config_parser().build_headers("accept_language_sas")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("CheckCoverage",
                                                                                "TAMMSubscriptionStandalone",
                                                                                "checkCoverage",
                                                                                headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    def test_check_in_process_application(self, api_helper):
        """Test checkInProcessApplication: BUAH-3666"""
        headers = api_helper.config_parser().build_headers("accept_language_sas")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("CheckInProcessApplication",
                                                                                "TAMMSubscriptionStandalone",
                                                                                "checkInProcessApplication",
                                                                                headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    def test_get_permit_rules_non_emirates_user(self, api_helper):
        """Test getPermitRules non Emirates user: BUAH-3667"""
        headers = api_helper.config_parser().build_headers("accept_language_sas")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetPermitRules",
                                                                                "TAMMSubscriptionStandalone",
                                                                                "getPermitRulesNoneEmiratesUser",
                                                                                headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    def test_get_permit_rules_emirates_user(self, api_helper):
        """Test getPermitRules Emirates user: BUAH-3668"""
        headers = api_helper.config_parser().build_headers("accept_language_sas")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetPermitRules",
                                                                                "TAMMSubscriptionStandalone",
                                                                                "getPermitRulesEmiratesUser",
                                                                                headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    def test_get_mawaq_if_fines(self, api_helper):
        """Test getMawaqifFines: BUAH-3669"""
        headers = api_helper.config_parser().build_headers("accept_language_sas")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetMawaqifFines",
                                                                                "TAMMSubscriptionStandalone",
                                                                                "getMawaqifFines",
                                                                                headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    def test_get_mawaq_if_fines_hossam(self, api_helper):
        """Test getMawaqifFines Hossam: BUAH-3670"""
        headers = api_helper.config_parser().build_headers("accept_language_sas")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("GetMawaqifFines",
                                                                                "TAMMSubscriptionStandalone",
                                                                                "getMawaqifFinesHossam",
                                                                                headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    def test_init_mawaq_if_permit_emirates_user(self, api_helper):
        """Test initializePermitRequest Emirate user: BUAH-367"""
        headers = api_helper.config_parser().build_headers("accept_language_sas")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("InitializePermitRequest",
                                                                                "TAMMSubscriptionStandalone",
                                                                                "initializePermitRequestEmiratesUser",
                                                                                headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    def test_init_mawaq_if_permit_non_emirates_user(self, api_helper):
        """Test initializePermitRequest non Emirate user: BUAH-3672"""
        headers = api_helper.config_parser().build_headers("accept_language_sas")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("InitializePermitRequest",
                                                                                "TAMMSubscriptionStandalone",
                                                                                "initializePermitRequestNonEmiratesUser"
                                                                                , headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    def test_init_mawaq_if_permit_non_emirates_user_hossam(self, api_helper): #500 error + Copy method
        """Test initializePermitRequest non Emirate user Hossam: BUAH-3673"""
        headers = api_helper.config_parser().build_headers("accept_language_sas")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("InitializePermitRequest",
                                                                                "TAMMSubscriptionStandalone",
                                                                                "initializePermitRequestNonEmiratesUser"
                                                                                "Hossam", headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    def test_finalize_permit_requset_non_emirates_user(self, api_helper):
        """Test finalizePermitRequest non Emirate user: BUAH-3674"""
        headers = api_helper.config_parser().build_headers("accept_language_sas")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("FinalizePermitRequest",
                                                                                "TAMMSubscriptionStandalone",
                                                                                "finalizePermitRequestNonEmiratesUser"
                                                                                , headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    def test_finalize_permit_requset_non_emirates_user_hossam(self, api_helper):  #500 error
        """Test finalizePermitRequest non Emirate user Hossam: BUAH-3675"""
        headers = api_helper.config_parser().build_headers("accept_language_sas")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("FinalizePermitRequest",
                                                                                "TAMMSubscriptionStandalone",
                                                                                "finalizePermitRequestNonEmiratesUser"
                                                                                "Hossam", headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    def test_finalize_permit_requset_emirates_user(self, api_helper):  #500 error
        """Test finalizePermitRequest Emirate user: BUAH-3676"""
        headers = api_helper.config_parser().build_headers("accept_language_sas")
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("FinalizePermitRequest",
                                                                                "TAMMSubscriptionStandalone",
                                                                                "finalizePermitRequestEmiratesUser"
                                                                                , headers=headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"