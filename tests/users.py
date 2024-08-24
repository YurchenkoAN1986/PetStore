import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import requests

from funcs import HOST, assert_res

# предполагается, что в системе нет пользователя с username test


class TestUser:
    def test_create_user(self):
        res = requests.post(
            url=f"{HOST}/user",
            json={
                "id": 0,
                "username": "test",
                "firstName": "test",
                "lastName": "test",
                "email": "test@test.test",
                "password": "testtest",
                "phone": "+79999999999",
                "userStatus": 0,
            },
        )

        assert_res(res=res, status_code=200)

    def test_login(self):
        res = requests.get(
            url=f"{HOST}/user/login",
            params={
                "username": "test",
                "password": "testtest",
            },
        )

        assert_res(res=res, status_code=200)

    def test_update_user(self):
        res = requests.put(
            url=f"{HOST}/user/test",
            json={
                "id": 0,
                "username": "test",
                "firstName": "test_upd_fn",
                "lastName": "test_upd_ln",
                "email": "test_upd_email",
                "password": "testtest",
                "phone": "+79999999988",
                "userStatus": 0,
            },
        )

        assert_res(res=res, status_code=200)

        self.test_delete_user(username="test", status_code=200)

        user = requests.get(url=f"{HOST}/user/test").json()

        assert all(
            user[key] == value
            for key, value in {
                "username": "test",
                "firstName": "test_upd_fn",
                "lastName": "test_upd_ln",
                "email": "test_upd_email",
                "password": "testtest",
                "phone": "+79999999988",
            }.items()
        )

    def test_logout(self):
        res = requests.get(url=f"{HOST}/user/logout")

        assert_res(res=res, status_code=200)

    def test_get_user(
        self,
        username: str = "test",
        status_code: int = 200,
    ):
        res = requests.get(url=f"{HOST}/user/{username}")

        assert_res(res=res, status_code=status_code)

    def test_delete_user(
        self,
        username: str = "test",
        status_code: int = 404,
    ):
        res = requests.delete(url=f"{HOST}/user/{username}")

        assert_res(res=res, status_code=200)

        self.test_get_user(username="test", status_code=status_code)

    def test_create_user_with_list(self):
        res = requests.post(
            url=f"{HOST}/user/createWithArray",
            json=[
                {
                    "id": 0,
                    "username": "test",
                    "firstName": "test",
                    "lastName": "test",
                    "email": "test@test.test",
                    "password": "testtest",
                    "phone": "+79999999999",
                    "userStatus": 0,
                },
                {
                    "id": 1,
                    "username": "test1",
                    "firstName": "test1",
                    "lastName": "test1",
                    "email": "test1@test.test",
                    "password": "testtest",
                    "phone": "+79999999998",
                    "userStatus": 0,
                },
            ],
        )

        assert_res(res=res, status_code=200)

        self.test_get_user(username="test")
        self.test_get_user(username="test1")

        self.test_delete_user(username="test")
        self.test_delete_user(username="test1")
