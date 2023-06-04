import random


class DataHelper:

    def __init__(self, task_set):
        self.task_set = task_set

    @classmethod
    def get_random_username(cls):
        return "userqa" + str(random.randint(1, 10000000))

    @classmethod
    def get_random_number(cls):
        return random.randint(1, 10000000)

    @classmethod
    def post_user_create_json(cls, username, id):
        payload = {
            "id": id,
            "username": username,
            "firstName": "test",
            "lastName": "qa",
            "email": "test@udemig.com",
            "password": "test123",
            "phone": "566555263662",
            "userStatus": 0
        }
        file = open("data/users.txt", "a")
        file.write(username + "\n")
        return payload

    @classmethod
    def get_random_file_username(cls):
        user_list = open("data/users.txt").read().splitlines()
        user = random.choice(user_list)
        return user

    @classmethod
    def get_login_payload(cls, username):
        payload = {"username": username, "password": "test123"}
        return payload