import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import requests

from funcs import HOST, assert_res

vars = {"order_id": None}


class TestStore:
    def test_create_order(self):
        res = requests.post(
            url=f"{HOST}/store/order",
            json={
                "id": 0,
                "petId": 0,
                "quantity": 0,
                "shipDate": "2021-09-01T12:00:00Z",
                "status": "placed",
                "complete": False,
            },
        )

        assert_res(res=res, status_code=200)

        vars["order_id"] = res.json()["id"]

    def test_get_order(self):
        res = requests.get(url=f"{HOST}/store/order/{vars['order_id']}")

        assert_res(res=res, status_code=200)

    def test_delete_order(self):
        res = requests.delete(url=f"{HOST}/store/order/{vars['order_id']}")

        assert_res(res=res, status_code=200)

    def test_inventory(self):
        res = requests.get(url=f"{HOST}/store/inventory")

        assert_res(res=res, status_code=200)
