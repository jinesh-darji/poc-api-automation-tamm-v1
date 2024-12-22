import sys

from locust import TaskSet, HttpLocust, task
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from hd_load import load_test_helper


class HD(TaskSet):

    @task(1)
    def test_1(self):
        load_test_helper.get(self.client, "test_1")

    @task(2)
    def test_2(self):
        load_test_helper.get(self.client, "test_2")


class AllTests(HttpLocust):
    host = load_test_helper.host
    task_set = HD
    min_wait = 5000
    max_wait = 15000
