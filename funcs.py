from requests import Response

HOST = "https://petstore.swagger.io/v2"

def assert_res(res: Response, status_code):
    if res.status_code != status_code:
        assert (
            False
        ), f"Bad status code: {res.status_code}. Expected: {status_code}. Url: {res.url}. Response: {res.text}"