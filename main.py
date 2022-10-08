import requests


def get_ip_info(ip: str = '') -> dict:
    url = f'http://ip-api.com/json/{ip}'

    try:
        return requests.get(url).json()

    except requests.exceptions.ConnectionError:
        raise 'Connection failed'