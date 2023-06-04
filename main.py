from locust import HttpUser, between, task
from helper.data_helper import DataHelper

class WebsiteUser(HttpUser):

    def __init__(self):
        self.data_helper = DataHelper(self)

    @task
    def get_username(self):
        username = self.data_helper.get_random_username()
        self.client.get("/v2/user/"+username)

    @task
    def post_user_create(self):
        user_create_json= {
  "id": 112155541121213,
  "username": "testqaudemig",
  "firstName": "test",
  "lastName": "qa",
  "email": "test@udemig.com",
  "password": "test123",
  "phone": "566555263662",
  "userStatus": 0
}
        self.client.post("/v2/user", json=user_create_json)

    @task
    def get_logout(self):
        self.client.get("/v2/user/logout")

    @task
    def get_login(self):
        login_params = {"username": "testqaudemig", "password": "test123"}
        self.client.get("/v2/user/login", params=login_params)

    @task
    def delete_user(self):
        user_create_json = {
            "id": 112155541121213,
            "username": "testqaudemig",
            "firstName": "test",
            "lastName": "qa",
            "email": "test@udemig.com",
            "password": "test123",
            "phone": "566555263662",
            "userStatus": 0
        }
        self.client.post("/v2/user", json=user_create_json)
        self.client.delete("/v2/user/testqaudemig")

    # @task
    # def get_user_list(self):
    #     login_params2 = {"username": "testqaudemig", "password": "test123"}
    #     login_params = {"username": "testqaudemig", "password": "test123"}
    #     self.client.get("/v2/userList", headers=login_params, json=login_params2, params={"username": "x"})