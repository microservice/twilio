from http import HTTPStatus
import ast
import os
import json

def test_sms_request(client):
    fromNumber = os.getenv('FROM_NUMBER_OK')
    toNumber = os.getenv('TO_NUMBER_OK')
    data = {
        "body": "Hello world !",
        "from": fromNumber,
        "to":  toNumber,
    }
    url = "/sms"
    response = client.post(url, json=data)
    assert response.status_code == HTTPStatus.OK

def test_sms_request_fail(client):
    fromNumber = os.getenv('FROM_NUMBER_INCORRECT')
    toNumber = os.getenv('TO_NUMBER_INCORRECT')
    data = {
        "body": "Hello world !",
        "from": fromNumber,
        "to":  toNumber,
    }
    url = "/sms"
    response = client.post(url, json=data)
    data = json.loads(response.data)
    assert data["status"] == HTTPStatus.BAD_REQUEST
