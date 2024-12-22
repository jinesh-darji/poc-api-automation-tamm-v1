import pytest
import configparser
import sys,os
sys.path.append(os.path.abspath('../'))
from utils.api_library import ApiMethods,Status
from test_data_configuration.test_data_config_parser import Config_parser
from utils import json_parser

''' Configuring environment & application variable as a input parameter '''
application_name=sys.argv[1]
environment_type=sys.argv[3]


'''Create an object with the environment values  and  particular journey name '''
config_value=Config_parser(application_name,environment_type,"protocal_http")

'''Getting initial URL from configuration file'''
main_url=config_value.main_url()

''' Building the headers from the configuration file '''
headers,inventoryheaders,emptyheaders,Invalidheaders,Invaliduserheaders=config_value.build_headers()

''' Object for to access all the library functions '''
libclient = ApiMethods(main_url)

'''#get the end_point into your test scripts based on the test data
#Ex. end_point=config_value.endpoint_parser('notification_health')
'''

''' In the following test cases only the response code will be checked for the services '''


class Test_cases_core(object):

    def test_to_chk_moi_health(self):
        end_point = config_value.endpoint_parser('moi_health')
        resp_code,resp_body,resp_time = libclient.get_response_data(end_point,headers)
        assert resp_code == Status.SUCCESS, "failed"

    def test_to_chk_moi_health_personprofile(self):
        end_point = config_value.endpoint_parser('moi_with_profile')
        resp_code, resp_body, resp_time = libclient.get_response_data(end_point, headers)
        assert resp_code == Status.SUCCESS, "failed"

    # def test_for_to_chk_get_data(self):
    #     end_point = config_value.endpoint_parser('notification_health')
    #     resp_code,resp_body,resp_time = libclient.get_response_data(end_point,headers)
    #     assert resp_code == Status.SUCCESS, "failed"
    # def test_for_to_chk_put_data(self):
    #     end_point = config_value.endpoint_parser('notification_health')
    #     body = json_parser.create_payload_for_service("notification")
    #     resp_code, resp_body, resp_time = libclient.put_response_data(end_point,body, headers)
    #     assert resp_code == Status.SUCCESS, "failed"


    # def test_to_chk_list_of_available_countries(self):
    #     end_point = config_value.endpoint_parser('visa_app_countries')
    #     resp_code,resp_body,resp_time = libclient.get_response_data(end_point,headers)
    #     assert resp_code == Status.SUCCESS, "failed"

