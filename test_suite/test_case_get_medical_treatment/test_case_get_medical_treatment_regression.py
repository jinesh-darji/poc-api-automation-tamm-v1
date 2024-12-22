import sys, os

sys.path.append(os.path.abspath('../'))
from utils import json_parser
from utils.api_library import ApiMethods, Status
from test_data_configuration.test_data_config_parser import Config_parser

''' Configuring environment & application variable as a input parameter '''
application_name = sys.argv[1]
environment_type = sys.argv[3]

'''Create an object with the environment values  and  particular journey name '''
config_value = Config_parser(application_name, environment_type, "protocol_https")

'''Getting initial URL from configuration file'''
main_url = config_value.main_url()

''' Building the headers from the configuration file '''
headers = config_value.build_headers("core_header")

''' Object for to access all the library functions '''
libclient = ApiMethods(main_url)

'''#get the end_point into your test scripts based on the test data
#Ex. end_point=config_value.endpoint_parser('notification_health')
'''

''' In the following test cases only the response code will be checked for the services '''


class Test_cases_gmtt(object):
    #
    # def test_getTRfVehicles(self):
    #     end_point = config_value.endpoint_parser('getTRfVehicles')
    #     body = json_parser.create_payload_for_service('VehicleService', 'getTRfVehicles', 'basic')
    #     resp_code, resp_body, resp_time, resp_headers = libclient.put_response_data(end_point, body, headers)
    #     assert resp_code == Status.SUCCESS, "failed"
    #     assert resp_headers.get(
    #         'ErrorDescriptionE') is None, "Response headers contains error :  %s" % resp_headers.get(
    #         'ErrorDescriptionE')
    #     assert json_parser.validate_response('VehicleService', "getTRfVehicles", resp_body), "failed"

    ''' Test cases related to DOH_IpcService '''

    def test_to_chk_IPCTRFApplicationStatus(self):
        end_point = config_value.endpoint_parser('IPCTRFApplicationStatus')
        body = json_parser.create_payload_for_service('DOH_IpcService', 'IPCTRFApplicationStatus')
        resp_code, resp_body, resp_time, resp_headers = libclient.put_response_data(end_point, body, headers)
        assert resp_code == Status.SUCCESS, "failed"
        assert json_parser.validate_response('DOH_IpcService', 'IPCTRFApplicationStatus', resp_body), "failed"

    ''' Test cases related to DOH_LookupService '''

    def test_to_chk_getCity(self):
        end_point = config_value.endpoint_parser('getCity')
        body = json_parser.create_payload_for_service('DOH_LookupService', 'getCity')
        resp_code, resp_body, resp_time, resp_headers = libclient.put_response_data(end_point, body, headers)
        assert resp_code == Status.SUCCESS, "failed"
        assert json_parser.validate_response('DOH_LookupService', 'getCity', resp_body), "failed"

    def test_to_chk_getFacilitySubType(self):
        end_point = config_value.endpoint_parser('getFacilitySubType')
        body = json_parser.create_payload_for_service('DOH_LookupService', 'getFacilitySubType')
        resp_code, resp_body, resp_time, resp_headers = libclient.put_response_data(end_point, body, headers)
        assert resp_code == Status.SUCCESS, "failed"
        assert json_parser.validate_response('DOH_LookupService', 'getFacilitySubType', resp_body), "failed"

    def test_to_chk_getFacilityType(self):
        end_point = config_value.endpoint_parser('getFacilitySubType')
        body = json_parser.create_payload_for_service('DOH_LookupService', 'getFacilitySubType')
        resp_code, resp_body, resp_time, resp_headers = libclient.put_response_data(end_point, body, headers)
        assert resp_code == Status.SUCCESS, "failed"
        assert json_parser.validate_response('DOH_LookupService', 'getFacilitySubType', resp_body), "failed"

    def test_to_chk_getGender(self):
        end_point = config_value.endpoint_parser('getGender')
        body = json_parser.create_payload_for_service('DOH_LookupService', 'getGender')
        resp_code, resp_body, resp_time, resp_headers = libclient.put_response_data(end_point, body, headers)
        assert resp_code == Status.SUCCESS, "failed"
        assert json_parser.validate_response('DOH_LookupService', 'getGender', resp_body), "failed"

    def test_to_chk_getIPCLookUPs(self):
        end_point = config_value.endpoint_parser('getIPCLookUPs')
        body = json_parser.create_payload_for_service('DOH_LookupService', 'getIPCLookUPs')
        resp_code, resp_body, resp_time, resp_headers = libclient.put_response_data(end_point, body, headers)
        assert resp_code == Status.SUCCESS, "failed"
        assert json_parser.validate_response('DOH_LookupService', 'getIPCLookUPs', resp_body), "failed"

    def test_to_chk_getNationality(self):
        end_point = config_value.endpoint_parser('getNationality')
        body = json_parser.create_payload_for_service('DOH_LookupService', 'getNationality')
        resp_code, resp_body, resp_time, resp_headers = libclient.put_response_data(end_point, body, headers)
        assert resp_code == Status.SUCCESS, "failed"
        assert json_parser.validate_response('DOH_LookupService', 'getNationality', resp_body), "failed"

    def test_to_chk_getProfession(self):
        end_point = config_value.endpoint_parser('getProfession')
        body = json_parser.create_payload_for_service('DOH_LookupService', 'getProfession')
        resp_code, resp_body, resp_time, resp_headers = libclient.put_response_data(end_point, body, headers)
        assert resp_code == Status.SUCCESS, "failed"
        assert json_parser.validate_response('DOH_LookupService', 'getProfession', resp_body), "failed"

    def test_to_chk_getSpecialty(self):
        end_point = config_value.endpoint_parser('getSpecialty')
        body = json_parser.create_payload_for_service('DOH_LookupService', 'getSpecialty')
        resp_code, resp_body, resp_time, resp_headers = libclient.put_response_data(end_point, body, headers)
        assert resp_code == Status.SUCCESS, "failed"
        assert json_parser.validate_response('DOH_LookupService', 'getSpecialty', resp_body), "failed"
