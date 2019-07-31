# -*- coding: utf-8 -*-
import json
import os
import sys

from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client

from flask import Flask, make_response, request


class Handler:
    app = Flask(__name__)

    def __init__(self) -> None:
        super().__init__()
        self.client = Client(os.getenv('ACCOUNT_SID'), os.getenv('AUTH_TOKEN'))

    def sms(self):
        req = request.get_json()
        try:
            message = self.client.messages \
                .create(body=req['body'], from_=req['from'], to=req['to'])
        except TwilioRestException as e:
            return self.end({
                'error_code': e.code, 'error_message': e.msg,
                'status': e.status, 'uri': e.uri
            })

        return self.end(
            {
                'error_code': message.error_code,
                'error_message': message.error_message,
                'status': message.status, 'price': message.price,
                'price_unit': message.price_unit,
                'sid': message.sid, 'uri': message.uri,
                'messaging_service_uid': message.messaging_service_sid
            })

    @staticmethod
    def end(res):
        resp = make_response(json.dumps(res))
        resp.headers['Content-Type'] = 'application/json; charset=utf-8'
        return resp


if __name__ == '__main__':
    if os.getenv('ACCOUNT_SID') is None or os.getenv('AUTH_TOKEN') is None:
        print('Environment variable ACCOUNT_SID/AUTH_TOKEN not found.')
        sys.exit(1)

    handler = Handler()
    handler.app.add_url_rule('/sms', 'sms', handler.sms,
                             methods=['post'])
    handler.app.run(host='0.0.0.0', port=8000)
