from http import HTTPStatus

def test_sms_request(client):
    data = {
        "body": "Hello world !",
        "from": "+917020149563",
        "to":  "+917020149563",
    }
    url = "/sms"
    response = client.post(url, json=data)
    assert response.status_code == HTTPStatus.OK
