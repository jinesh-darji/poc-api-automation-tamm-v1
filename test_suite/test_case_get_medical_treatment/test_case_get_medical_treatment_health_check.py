
import sys,os
sys.path.append(os.path.abspath('../'))
from utils import json_parser
from utils.api_library import ApiMethods,Status
from test_data_configuration.test_data_config_parser import Config_parser


''' Configuring environment & application variable as a input parameter '''
application_name=sys.argv[1]
environment_type=sys.argv[3]


'''Create an object with the environment values  and  particular journey name '''
config_value=Config_parser(application_name,environment_type,"protocol_https")

'''Getting initial URL from configuration file'''
main_url=config_value.main_url()

''' Building the headers from the configuration file '''
headers = config_value.build_headers("core_header")

''' Object for to access all the library functions '''
libclient = ApiMethods(main_url)

'''#get the end_point into your test scripts based on the test data
#Ex. end_point=config_value.endpoint_parser('notification_health')
'''

''' In the following test cases only the response code will be checked for the services '''



class Test_cases_gmtt(object):

    ''' Test cases related to DOH_IpcService '''

    # def test_to_chk_IPCTRFApplicationStatus(self):
    #     end_point = config_value.endpoint_parser('IPCTRFApplicationStatus')
    #     body = json_parser.create_payload_for_service('DOH_IpcService','IPCTRFApplicationStatus')
    #     resp_code,resp_body,resp_time, resp_headers = libclient.put_response_data(end_point,body,headers)
    #     assert resp_code == Status.SUCCESS, "failed"
    #
    # def test_to_chk_IPCTRFGet(self):
    #     end_point = config_value.endpoint_parser('IPCTRFGet')
    #     body = json_parser.create_payload_for_service('DOH_IpcService','IPCTRFGetRequest')
    #     resp_code,resp_body,resp_time, resp_headers = libclient.put_response_data(end_point,body,headers)
    #     assert resp_code == Status.SUCCESS, "failed"
    #
    # def test_to_chk_IPCTRFStatusUpdate(self):
    #     end_point = config_value.endpoint_parser('IPCTRFStatusUpdate')
    #     body = json_parser.create_payload_for_service('DOH_IpcService','IPCTRFStatusUpdate')
    #     resp_code,resp_body,resp_time, resp_headers = libclient.put_response_data(end_point,body,headers)
    #     assert resp_code == Status.MISSING_SOURCE, "failed"
    #
    # def test_to_chk_IPCTRFSaveAttachement(self):
    #     end_point = config_value.endpoint_parser('IPCTRFSaveAttachement')
    #     body = json_parser.create_payload_for_service('DOH_IpcService','IPCTRFSaveAttachment')
    #     resp_code,resp_body,resp_time, resp_headers = libclient.put_response_data(end_point,body,headers)
    #     assert resp_code == Status.SUCCESS, "failed"

    ''' below testing throwing error for format in language for payload'''
    # def test_to_chk_IPCTRFSave(self):
    #     end_point = config_value.endpoint_parser('IPCTRFSave')
    #     body = json_parser.create_payload_for_service('DOH_IpcService','IPCTRFSave')
    #     resp_code,resp_body,resp_time, resp_headers = libclient.put_response_data(end_point,body,headers)
    #     assert resp_code == Status.SUCCESS, "failed"

    ''' Test cases related to DOH_LicensedService '''

    def test_to_chk_getHIBasicProduct(self):
        end_point = config_value.endpoint_parser('getHIBasicProduct')
        body = json_parser.create_payload_for_service('DOH_LicensedService','getHIBasicProduct')
        resp_code,resp_body,resp_time, resp_headers = libclient.put_response_data(end_point,body,headers)
        assert resp_code == Status.SUCCESS, "failed"

    def test_to_chk_getHICompanyList(self):
        end_point = config_value.endpoint_parser('getHICompanyList')
        body = json_parser.create_payload_for_service('DOH_LicensedService', 'getHICompanyList')
        resp_code, resp_body, resp_time, resp_headers = libclient.put_response_data(end_point, body, headers)
        assert resp_code == Status.SUCCESS, "failed"

    def test_to_chk_getHIEnhancedProduct(self):
        end_point = config_value.endpoint_parser('getHIEnhancedProduct')
        body = json_parser.create_payload_for_service('DOH_LicensedService', 'getHIEnhancedProduct')
        resp_code, resp_body, resp_time, resp_headers = libclient.put_response_data(end_point, body, headers)
        assert resp_code == Status.SUCCESS, "failed"

    def test_to_chk_getHIVisitorProduct(self):
        end_point = config_value.endpoint_parser('getHIVisitorProduct')
        body = json_parser.create_payload_for_service('DOH_LicensedService', 'getHIVisitorProduct')
        resp_code, resp_body, resp_time, resp_headers = libclient.put_response_data(end_point, body, headers)
        assert resp_code == Status.SUCCESS, "failed"

    def test_to_chk_getMedicalFacilities(self):
        end_point = config_value.endpoint_parser('getMedicalFacilities')
        body = json_parser.create_payload_for_service('DOH_LicensedService', 'getMedicalFacilities')
        resp_code, resp_body, resp_time, resp_headers = libclient.put_response_data(end_point, body, headers)
        assert resp_code == Status.SUCCESS, "failed"

    def test_to_chk_getMedicalProfEducation(self):
        end_point = config_value.endpoint_parser('getMedicalProfEducation')
        body = json_parser.create_payload_for_service('DOH_LicensedService', 'getMedicalProfEducation')
        resp_code, resp_body, resp_time, resp_headers = libclient.put_response_data(end_point, body, headers)
        assert resp_code == Status.SUCCESS, "failed"

    def test_to_chk_getMedicalProfExperience(self):
        end_point = config_value.endpoint_parser('getMedicalProfExperience')
        body = json_parser.create_payload_for_service('DOH_LicensedService', 'getMedicalProfExperience')
        resp_code, resp_body, resp_time, resp_headers = libclient.put_response_data(end_point, body, headers)
        assert resp_code == Status.SUCCESS, "failed"

    def test_to_chk_getMedicalProfessional(self):
        end_point = config_value.endpoint_parser('getMedicalProfessional')
        body = json_parser.create_payload_for_service('DOH_LicensedService', 'getMedicalProfessional')
        resp_code, resp_body, resp_time, resp_headers = libclient.put_response_data(end_point, body, headers)
        assert resp_code == Status.SUCCESS, "failed"

    ''' Test cases related to DOH_LookupService '''
    #
    # def test_to_chk_getCity(self):
    #     end_point = config_value.endpoint_parser('getCity')
    #     body = json_parser.create_payload_for_service('DOH_LookupService', 'getCity')
    #     resp_code, resp_body, resp_time, resp_headers = libclient.put_response_data(end_point, body, headers)
    #     assert resp_code == Status.SUCCESS, "failed"
    #
    # def test_to_chk_getFacilitySubType(self):
    #     end_point = config_value.endpoint_parser('getFacilitySubType')
    #     body = json_parser.create_payload_for_service('DOH_LookupService', 'getFacilitySubType')
    #     resp_code, resp_body, resp_time, resp_headers = libclient.put_response_data(end_point, body, headers)
    #     assert resp_code == Status.SUCCESS, "failed"
    #
    # def test_to_chk_getFacilityType(self):
    #     end_point = config_value.endpoint_parser('getFacilityType')
    #     body = json_parser.create_payload_for_service('DOH_LookupService', 'getFacilityType')
    #     resp_code, resp_body, resp_time, resp_headers = libclient.put_response_data(end_point, body, headers)
    #     assert resp_code == Status.SUCCESS, "failed"
    #
    # def test_to_chk_getGender(self):
    #     end_point = config_value.endpoint_parser('getGender')
    #     body = json_parser.create_payload_for_service('DOH_LookupService', 'getGender')
    #     resp_code, resp_body, resp_time, resp_headers = libclient.put_response_data(end_point, body, headers)
    #     assert resp_code == Status.SUCCESS, "failed"
    #
    # def test_to_chk_getIPCLookUPs(self):
    #     end_point = config_value.endpoint_parser('getIPCLookUPs')
    #     body = json_parser.create_payload_for_service('DOH_LookupService', 'getIPCLookUPs')
    #     resp_code, resp_body, resp_time, resp_headers = libclient.put_response_data(end_point, body, headers)
    #     assert resp_code == Status.SUCCESS, "failed"
    #
    # def test_to_chk_getNationality(self):
    #     end_point = config_value.endpoint_parser('getNationality')
    #     body = json_parser.create_payload_for_service('DOH_LookupService', 'getNationality')
    #     resp_code, resp_body, resp_time, resp_headers = libclient.put_response_data(end_point, body, headers)
    #     assert resp_code == Status.SUCCESS, "failed"
    #
    # def test_to_chk_getProfession(self):
    #     end_point = config_value.endpoint_parser('getProfession')
    #     body = json_parser.create_payload_for_service('DOH_LookupService', 'getProfession')
    #     resp_code, resp_body, resp_time, resp_headers = libclient.put_response_data(end_point, body, headers)
    #     assert resp_code == Status.SUCCESS, "failed"
    #

    ''' Test cases related to DOH_MiscellaneousService  '''

    def test_to_chk_GetDOHDrugsList(self):
        end_point = config_value.endpoint_parser('GetDOHDrugsList')
        body = json_parser.create_payload_for_service('DOH_MiscellaneousService', 'GetDOHDrugsList')
        resp_code, resp_body, resp_time, resp_headers = libclient.put_response_data(end_point, body, headers)
        assert resp_code == Status.SUCCESS, "failed"

    def test_to_chk_GetPublicHealthInformation(self):
        end_point = config_value.endpoint_parser('GetPublicHealthInformation')
        body = json_parser.create_payload_for_service('DOH_MiscellaneousService', 'GetPublicHealthInformation')
        resp_code, resp_body, resp_time, resp_headers = libclient.put_response_data(end_point, body, headers)
        assert resp_code == Status.SUCCESS, "failed"

    def test_to_chk_GetSickLeaveDetails(self):
        end_point = config_value.endpoint_parser('GetSickLeaveDetails')
        body = json_parser.create_payload_for_service('DOH_MiscellaneousService', 'GetSickLeaveDetails')
        resp_code, resp_body, resp_time, resp_headers = libclient.put_response_data(end_point, body, headers)
        assert resp_code == Status.SUCCESS, "failed"

