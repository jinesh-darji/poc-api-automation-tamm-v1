from locust import TaskSet, task, HttpLocust
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from buy_a_home_load import load_test_helper


class BuyAHome(TaskSet):

    @task(4)
    def OpLeadStatusInquiry(self):
        load_test_helper.post(self.client, "OpLeadStatusInquiry",
                              "LeadManagementR",
                              "getOpLeadStatusInquiry")


class AllTests(HttpLocust):
    host = load_test_helper.host
    task_set = BuyAHome
    min_wait = 5000
    max_wait = 15000
