from utils.api_library import Status

"""In the following test cases only the response code will be checked for the services"""


class TestTemplateHealthCheck(object):

    def test_template_endpoint_get_response(self, api_helper):
        """
        parameter in get_response method is the name of your endpoint in template.conf file
        """
        resp_code, resp_body, resp_time, resp_header = api_helper.get_response("template_name_of_endpoint")
        assert resp_code == Status.SUCCESS, "Template endpoint response is not 200"

    def test_template_endpoint_post_response(self, api_helper):
        """ The first parameter in this method refers to the name of endpoint in template.conf file.
            The second parameter is the name of your folder in template/request directory
            the third parameter is the name of your endpoint inside the folder from the second parameter
            (e.g. for template_name_of_endpoint_main.json it will be "template_name_of_endpoint")
        """
        resp_code, resp_body, resp_time, resp_header = api_helper.post_response("template_name_of_endpoint",
                                                                                "template_name_of_API",
                                                                                "template_name_of_endpoint")
        assert resp_code == Status.SUCCESS, "Nationality Check response code is not 200"


