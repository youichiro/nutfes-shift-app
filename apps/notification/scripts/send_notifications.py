# -*- coding: utf-8 -*-
import json
import requests
from tqdm import tqdm
from apps.notification.models import DeviceToken


def send_notification(title, body):
    """タイトルと本文を通知する"""
    for device_token in DeviceToken.uniq_list():
        token = device_token.token
        data = {
            'to': token,
            'title': title,
            'body': body,
            'data': {
                'title': title,
                'body': body,
            }
        }
        post_request(data)


def post_request(data):
    """通知するためのAPIを叩く"""
    assert 'to' in data and 'body' in data and 'data' in data
    assert 'body' in data['data']
    requests.post(
        'https://exp.host/--/api/v2/push/send',
        json.dumps(data),
        headers={'Content-Type': 'application/json'}
    )


def main():
    filename = 'static/json/next_push_requests.json'
    with open(filename) as f:
        push_requests = json.load(f)
    for data in tqdm(push_requests):
        post_request(data)
    print('Finish sending push notifications')
