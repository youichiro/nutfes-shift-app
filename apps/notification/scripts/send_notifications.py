# -*- coding: utf-8 -*-
import json
import requests
from tqdm import tqdm


def post_request(data):
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
