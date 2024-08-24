import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import requests
from funcs import HOST, assert_res

vars = {"pet_id": None}

class TestPet:
    def test_create_pet(self):
        res = requests.post(
            url=f"{HOST}/pet",
            json={
                "id": 0,
                "category": {
                    "id": 0,
                    "name": "category",
                },
                "name": "cat",
                "photoUrls": [],
                "tags": [],
                "status": "available",
            },
        )

        assert_res(res=res, status_code = 200)
        vars["pet_id"]= res.json()["id"]

    def test_get_pet(self):
        res = requests.get(url=f"{HOST}/pet/{vars['pet_id']}")

        assert_res(res=res, status_code=200)

    def test_update_pet(self):
        res = requests.put(
            url=f"{HOST}/pet",
            json={
                "id": vars["pet_id"],
                "category": {
                    "id": 0,
                    "name": "category",
                },
                "name": "cat_upd",
                "photoUrls": [],
                "tags": [],
                "status": "available",
            },
        )

        assert_res(res = res, status_code=200)

    def test_upload_image(self):
        res = requests.post(
            url=f"{HOST}/pet/{vars['pet_id']}/uploadImage",
            files={"file": open("./assets/image.jpeg", "rb")},
        )
        assert_res(res= res, status_code=200)

        # def test_delete_pet(self):
        #     res = requests.delete(url=f"{HOST}/pet/{vars['pet_id']}")
        #
        #     assert_res(res=res, status_code=200)
        #
        #     res = requests.get(url=f"{HOST}/pet/{vars["pet_id"]}")
        #
        #     assert_res(res=res, status_code=404)

        def test_find_by_status(self):
            res = requests.get(url=f"{HOST}/pet/findByStatus?status=available")

            assert_res(res=res, status_code=200)
