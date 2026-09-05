import requests
import pytest

BASE_URL = 'https://jsonplaceholder.typicode.com'


def test_protected_endpoint_without_token():
    response = requests.get(f'{BASE_URL}/private/data')
    assert response.status_code == 401


def test_protected_endpoint_with_token():
    headers = {'Authorization': 'Bearer some-valid-token-here'}
    response = requests.get(f'{BASE_URL}/private/data')
    assert response.status_code == 200