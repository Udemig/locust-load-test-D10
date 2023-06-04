from locust import HttpUser, between
from task_set.user_task_set import UserTaskSet

class PetstoreUserTest(HttpUser):
    wait_time = between(1, 2)
    tasks = {
        UserTaskSet
    }