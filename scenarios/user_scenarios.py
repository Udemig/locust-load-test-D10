class UserScenarios:

    def __init__(self, task_set):
        self.task_set = task_set

    def get_username(self, user):
        self.task_set.client.get("/v2/user/"+user, name="/v2/user/{username}")

    def post_user_create(self, user_create_json):
        self.task_set.client.post("/v2/user", json=user_create_json)

    def get_logout(self):
        self.task_set.client.get("/v2/user/logout", name="/v2/user/logout")

    def get_login(self, login_params):
        self.task_set.client.get("/v2/user/login", name="/v2/user/login", params=login_params)

    def delete_user(self, user):
        self.task_set.client.delete("/v2/user/"+user, name="/v2/user/{username}")