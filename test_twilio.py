from http import HTTPStatus
import ast
import json

def test_sms_request(client):
    data = {
        "body": "Hello world !",
        "from": "+17042456341",
        "to":  "+917507704328",
    }
    url = "/sms"
    response = client.post(url, json=data)
    assert response.status_code == HTTPStatus.OK

def test_sms_request_fail(client):
    data = {
        "body": "Hello world !",
        "from": "+17042456341",
        "to":  "+112233445566",
    }
    url = "/sms"
    response = client.post(url, json=data)
    data = json.loads(response.data)
    assert data["status"] == HTTPStatus.BAD_REQUEST