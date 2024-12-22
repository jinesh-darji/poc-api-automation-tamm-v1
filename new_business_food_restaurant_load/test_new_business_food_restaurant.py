from locust import TaskSet, task, HttpLocust
import sys
from os import path
from new_business_food_restaurant_load import load_test_helper
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


class NewBusinessFoodRestaurant(TaskSet):

    """Test cases related to ADFCA"""

    @task(1)
    def StartNocProcess(self):
        load_test_helper.post(self.client, "startNocProcess", "ADFCA", "startNocProcess")

    @task(1)
    def GetNocStatus(self):
        load_test_helper.post(self.client, "getNocStatus", 'ADFCA', 'getNocStatus')

    @task(1)
    def GetInspectionDetails(self):
        load_test_helper.post(self.client, "getInspectionDetails", 'ADFCA', 'getInspectionDetails')

    @task(1)
    def SubmitPaymentDetails(self):
        load_test_helper.post(self.client, "submitPaymentDetails", 'ADFCA', 'submitPaymentDetails')

    @task(1)
    def GetPaymentDetails(self):
        load_test_helper.post(self.client, "getPaymentDetails", 'ADFCA', 'getPaymentDetails')

    @task(1)
    def GetCertificate(self):
        load_test_helper.post(self.client, "getCertificate", 'ADFCA', 'getCertificate')

    """Test cases related to ADJD"""

    @task(1)
    def GetPartnershipContract(self):
        load_test_helper.post(self.client, "getPartnershipContract", 'ADJD', 'getPartnershipContract')

    @task(1)
    def GetPartnershipContractDetails(self):
        load_test_helper.post(self.client, "getPartnershipContractDetails", 'ADJD', 'getPartnershipContractDetails')

    @task(1)
    def GetPartnershipContractInfo(self):
        load_test_helper.post(self.client, "getPartnershipContractInfo", 'ADJD', 'getPartnershipContractInfo')

    """Test cases related to ADM"""

    @task(1)
    def GetListOfConsultantsAndContractors(self):
        load_test_helper.post(self.client, "getListOfConsultantsAndContractors", "ADM",
                              "getListOfConsultantsAndContractors")

    @task(1)
    def GetToken(self):
        load_test_helper.post(self.client, "getToken", "ADM", "getToken")

    """Test cases related to DED"""

    @task(1)
    def AuthenticateUser(self):
        load_test_helper.post(self.client, "authenticateUser", "DED", "authenticateUser")

    @task(1)
    def BusinessLicense(self):
        load_test_helper.post(self.client, "businessLicense", "DED", "businessLicense")

    @task(1)
    def BusinessAmendment(self):
        load_test_helper.post(self.client, "businessAmendment", "DED", "businessAmendment")

    @task(1)
    def CheckApplicationStatus(self):
        load_test_helper.post(self.client, "checkApplicationStatus", 'DED', 'checkApplicationStatus')

    @task(1)
    def TradeNameCheck(self):
        load_test_helper.post(self.client, "tradeNameCheck", 'DED', 'tradeNameCheck',)

    @task(1)
    def BusinessName(self):
        load_test_helper.post(self.client, "businessName", 'DED', 'businessName')

    @task(1)
    def UploadDocument(self):
        load_test_helper.post(self.client, "uploadDocument", "DED", "uploadDocument")

    @task(1)
    def BusinessCertificate(self):
        load_test_helper.post(self.client, "businessCertificate", 'DED', 'businessCertificate')

    @task(1)
    def CheckLinkedLicense(self):
        load_test_helper.post(self.client, "checkLinkedLicense", 'DED', 'checkLinkedLicense', )

    @task(1)
    def GetFees(self):
        load_test_helper.post(self.client, "getFees", 'DED', 'getFees')

    @task(1)
    def ListTradeLicenses(self):
        load_test_helper.post(self.client, "listTradeLicenses", "DED", "listTradeLicenses")

    @task(1)
    def GetTradeLicenseDetails(self):
        load_test_helper.post(self.client, "getTradeLicenseDetails", 'DED', 'getTradeLicenseDetails')

    """Test cases related to DOH"""

    @task(1)
    def GetHealthInsurance(self):
        load_test_helper.post(self.client, "getHealthInsurance", 'DOH', 'getHealthInsurance')

    @task(1)
    def GetHealthInsuranceEmiratesID(self):
        load_test_helper.post(self.client, "getHealthInsuranceEmiratesID", 'DOH', 'getHealthInsuranceEmiratesID')

    @task(1)
    def GetFitnessCertificate(self):
        load_test_helper.post(self.client, "getFitnessCertificate", 'DOH', 'getFitnessCertificate')

    """Test cases related to Tawtheeq"""

    @task(1)
    def GetTawtheeqDetails(self):
        load_test_helper.post(self.client, "getTawtheeqDetails", 'Tawtheeq', 'getTawtheeqDetails')

    @task(1)
    def GetTawtheeqList(self):
        load_test_helper.post(self.client, "getTawtheeqList", 'Tawtheeq', 'getTawtheeqList')

    """Test cases related to ICA"""

    @task(1)
    def GetPersonProfileUnifiedNumber(self):
        load_test_helper.post(self.client, "getPersonProfileUnifiedNumber", 'ICA', 'getPersonProfileUnifiedNumber')

    @task(1)
    def GetPersonProfileIdentitiyCard(self):
        load_test_helper.post(self.client, "getPersonProfileIdentitiyCard", 'ICA', 'getPersonProfileIdentitiyCard')

    """Test cases related to Doc-converter"""

    @task(1)
    def ConvertDocument(self):
        load_test_helper.post(self.client, "convertDocument", 'Doc-converter', 'convertDocument')

    """Test cases related to ADAlerts"""

    @task(1)
    def EmailSendByAddress(self):
        load_test_helper.post(self.client, "emailSendByAddress", 'ADAlerts', 'emailSendByAddress')

    @task(1)
    def EmailSendByAddressWithAttachment(self):
        load_test_helper.post(self.client, "emailSendByAddressWithAttachment", 'ADAlerts',
                              'emailSendByAddressWithAttachment')


class AllTests(HttpLocust):
    host = load_test_helper.host
    task_set = NewBusinessFoodRestaurant
    min_wait = 5000
    max_wait = 15000
