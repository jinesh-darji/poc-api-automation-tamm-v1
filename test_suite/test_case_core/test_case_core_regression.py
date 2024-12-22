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

''' In the following test cases output response(Ex. attributes and text) will be checked for the services '''

class Test_cases_Journy1(object):

    # def test_for_to_verify_get_data_response(self):
    #     end_point = config_value.endpoint_parser('notification_health')
    #     resp_code, resp_body, resp_time = libclient.get_response_data(end_point, headers)
    #     ''' Compare the response with the existing response '''
    #     #assert resp_body == json_parser.JsonParser.read_json_file_to_string('../template/requests/',"notification_main"), "failed"

    def test_to_chk_moi_health_with_reponse(self):
        end_point = config_value.endpoint_parser('moi_with_profile')
        resp_code, resp_body, resp_time = libclient.get_response_data(end_point, headers)
        if resp_body["data"]["unifiedNumber"] and resp_code == Status.SUCCESS:
            passed = True
        assert passed == True, "failed"


