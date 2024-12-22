import sys
import os
sys.path.append(os.path.abspath('../'))
from utils import json_parser
from utils.api_library import ApiMethods
from utils.api_library import Status
from test_data_configuration.test_data_config_parser import Config_parser


''' Configuring environment & application variable as a input parameter '''
application_name = sys.argv[1]
environment_type = sys.argv[3]


'''Create an object with the environment values  and  particular journey name '''
config_value = Config_parser(application_name, environment_type, 'protocol_https')

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


class TestCasesADP(object):

    def test_getTRfVehicles(self):
        end_point = config_value.endpoint_parser('getTRfVehicles')
        body = json_parser.create_payload_for_service('VehicleService', 'getTRfVehicles', 'basic')
        resp_code, resp_body, resp_time, resp_headers = libclient.put_response_data(end_point, body, headers)
        assert resp_code == Status.SUCCESS, "failed"
        assert resp_headers.get(
            'ErrorDescriptionE') is None, "Response headers contains error :  %s" % resp_headers.get(
            'ErrorDescriptionE')
        # assert json_parser.validate_response('VehicleService', "getTRfVehicles", resp_body), "failed"

    def test_getVehicleDetails(self):
        end_point = config_value.endpoint_parser('getVehicleDetails')
        body = json_parser.create_payload_for_service('VehicleService', 'getVehicleDetails')
        resp_code, resp_body, resp_time, resp_headers = libclient.put_response_data(end_point, body, headers)
        assert resp_code == Status.SUCCESS, "failed"
        assert resp_headers.get(
            'ErrorDescriptionE') is None, "Response headers contains error :  %s" % resp_headers.get(
            'ErrorDescriptionE')
        assert json_parser.validate_response('VehicleService', "getVehicleDetails", resp_body), "failed"

    def test_getVehicleRestrictions(self):
        end_point = config_value.endpoint_parser('getVehicleRestrictions')
        body = json_parser.create_payload_for_service('VehicleService', 'getVehicleRestrictions')
        resp_code, resp_body, resp_time, resp_headers = libclient.put_response_data(end_point, body, headers)
        assert resp_code == Status.SUCCESS, "failed"
        assert resp_headers.get(
            'ErrorDescriptionE') is None, "Response headers contains error :  %s" %resp_headers.get(
            'ErrorDescriptionE')
        assert json_parser.validate_response('VehicleService', "getVehicleRestrictions", resp_body), "failed"

    def test_GetTrfNoByNationalID(self):
        end_point = config_value.endpoint_parser('GetTrfNoByNationalID')
        body = json_parser.create_payload_for_service('TrafficProfile', 'GetTrfNoByNationalID')
        resp_code, resp_body, resp_time, resp_headers = libclient.put_response_data(end_point, body, headers)
        assert resp_code == Status.SUCCESS, "failed"
        assert resp_headers.get(
            'ErrorDescriptionE') is None, "Response headers contains error :  %s" % resp_headers.get(
            'ErrorDescriptionE')
        assert json_parser.validate_response('TrafficProfile', 'GetTrfNoByNationalID', resp_body), "failed"

    def test_GetTrafficProfile(self):
        end_point = config_value.endpoint_parser('GetTrafficProfile')
        body = json_parser.create_payload_for_service('TrafficProfile', 'GetTrafficProfile')
        resp_code, resp_body, resp_time, resp_headers = libclient.put_response_data(end_point, body, headers)
        assert resp_code == Status.SUCCESS, "failed"
        assert resp_headers.get(
            'ErrorDescriptionE') is None, "Response headers contains error :  %s" % resp_headers.get(
            'ErrorDescriptionE')
        assert json_parser.validate_response('TrafficProfile', 'GetTrafficProfile', resp_body), "failed"

    def test_getVehicleServiceFees(self):
        end_point = config_value.endpoint_parser('getVehicleServiceFees')
        body = json_parser.create_payload_for_service('VehicleService', 'getVehicleServiceFees')
        resp_code, resp_body, resp_time, resp_headers = libclient.put_response_data(end_point, body, headers)
        assert resp_code == Status.SUCCESS, "failed"
        assert resp_headers.get(
            'ErrorDescriptionE') is None, "Response headers contains error :  %s" % resp_headers.get(
            'ErrorDescriptionE')
        # assert json_parser.validate_response('VehicleService', 'getVehicleServiceFees', resp_body), "failed"

    def test_getVehicleTickets(self):
        end_point = config_value.endpoint_parser('getVehicleTickets')
        body = json_parser.create_payload_for_service('VehicleService', 'getVehicleTickets')
        resp_code, resp_body, resp_time, resp_headers = libclient.put_response_data(end_point, body, headers)
        assert resp_code == Status.SUCCESS, "failed"
        assert resp_headers.get(
            'ErrorDescriptionE') is None, "Response headers contains error :  %s" % resp_headers.get(
            'ErrorDescriptionE')
        assert json_parser.validate_response('VehicleService', 'getVehicleTickets', resp_body), "failed"

    def test_GetUnifiedID(self):
        end_point = config_value.endpoint_parser('GetUnifiedID')
        body = json_parser.create_payload_for_service('TrafficProfile', 'GetUnifiedID')
        resp_code, resp_body, resp_time, resp_headers = libclient.put_response_data(end_point, body, headers)
        assert resp_code == Status.SUCCESS, "failed"
        assert resp_headers.get(
            'ErrorDescriptionE') is None, "Response headers contains error :  %s" % resp_headers.get(
            'ErrorDescriptionE')
        assert json_parser.validate_response('TrafficProfile', 'GetUnifiedID', resp_body), "failed"

    def test_GetTickets(self):
        end_point = config_value.endpoint_parser('GetTickets')
        body = json_parser.create_payload_for_service('TicketServices', 'GetTickets')
        resp_code, resp_body, resp_time, resp_headers = libclient.put_response_data(end_point, body, headers)
        assert resp_code == Status.SUCCESS, "failed"
        assert resp_headers.get(
            'ErrorDescriptionE') is None, "Response headers contains error :  %s" % resp_headers.get(
            'ErrorDescriptionE')
        assert json_parser.validate_response('TicketServices', 'GetTickets', resp_body), "failed"

    def test_getAccidentDetails(self):
        end_point = config_value.endpoint_parser('getAccidentDetails')
        body = json_parser.create_payload_for_service('AccidentServices', 'getAccidentDetails')
        resp_code, resp_body, resp_time, resp_headers = libclient.put_response_data(end_point, body, headers)
        assert resp_code == Status.SUCCESS, "failed"
        assert resp_headers.get(
            'ErrorDescriptionE') is None, "Response headers contains error :  %s" % resp_headers.get(
            'ErrorDescriptionE')
        assert json_parser.validate_response('AccidentServices', 'getAccidentDetails', resp_body), "failed"

    def test_getDriverAccidents(self):
        end_point = config_value.endpoint_parser('getDriverAccidents')
        body = json_parser.create_payload_for_service('AccidentServices', 'getDriverAccidents')
        resp_code, resp_body, resp_time, resp_headers = libclient.put_response_data(end_point, body, headers)
        assert resp_code == Status.SUCCESS, "failed"
        assert resp_headers.get(
            'ErrorDescriptionE') is None, "Response headers contains error :  %s" % resp_headers.get(
            'ErrorDescriptionE')
        assert json_parser.validate_response('AccidentServices', 'getDriverAccidents', resp_body), "failed"

#############################################################################################################
