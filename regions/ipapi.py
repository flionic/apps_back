import json

import requests


class RateLimitException(Exception):
    pass


def get_region(ip):
    region = None
    print('get_region')
    try:
        region = ipapico(ip)
    except RateLimitException:
        region = ip_api_com(ip)
    finally:
        return region


def ipapico(ip):
    print("ipapico")
    response = requests.get(f'https://ipapi.co/{ip}/country/')
    if response.status_code != 200:
        resp_json = json.loads(response.text.replace("'", '"').replace("True", 'true'))
        if resp_json['reason'] == 'RateLimited':
            raise RateLimitException
    if response.text == 'Undefined':
        return None
    return response.text


def ip_api_com(ip):
    print("ip_api_com")
    response = requests.get(f'http://ip-api.com/json/{ip}')
    if response.json()['status'] == 'fail':
        return None
    return response.json()['countryCode']
