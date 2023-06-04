from locust import TaskSet, task
from helper.data_helper import DataHelper
from scenarios.user_scenarios import UserScenarios

class UserTaskSet(TaskSet):

    def __init__(self, parent):
        super().__init__(parent)
        self.data_helper = DataHelper(self)
        self.user_scenarios = UserScenarios(self)

    @task
    def get_user(self):
        user = self.data_helper.get_random_file_username()
        self.user_scenarios.get_username(user)

    @task
    def post_user_create(self):
        user = self.data_helper.get_random_username()
        id = self.data_helper.get_random_number()
        user_create_json = self.data_helper.post_user_create_json(user, id)
        self.user_scenarios.post_user_create(user_create_json)

    @task
    def get_logout(self):
        self.user_scenarios.get_logout()

    @task
    def get_login(self):
        user = self.data_helper.get_random_username()
        user_payload = self.data_helper.get_login_payload(user)
        self.user_scenarios.get_login(user_payload)

    @task
    def delete_user(self):
        user = self.data_helper.get_random_file_username()
        self.user_scenarios.delete_user(user)