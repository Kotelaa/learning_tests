import requests
import pytest
from urllib3.util import parse_url

BASE_URL = 'https://jsonplaceholder.typicode.com'


@pytest.fixture
def valid_payload():
    return {'title': 'Test post', 'body': 'Content here', 'userID': 1}

@pytest.fixture
def valid_new_post():
    return {'title': 'New post', 'body': 'Post\'s content', 'userID': 1}


def test_get_single_post_another_test():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == 1
    assert "title" in data


def test_update_post():
    payload = {'title': 'Updated title'}
    response = requests.patch(f'{BASE_URL}/posts/1', json=payload)
    assert response.status_code == 200
    assert response.json()['title'] == 'Updated title'


def test_delete_post():
    response = requests.delete(f'{BASE_URL}/posts/1')
    assert response.status_code == 204


def test_create_post_missing_required_field():
    payload = {'body': 'No title here'}
    response = requests.post(f'{BASE_URL}/posts', json=payload)
    print(response.status_code, response.json())


@pytest.mark.parametrize('post_id', 'expected_status', [
    (1, 200),
    (100, 200),
    (9999999, 404)
])
def test_get_post_various_ids(post_id, expected_status):
    response = requests.get(f'{BASE_URL}/posts/{post_id}')
    assert response.status_code == expected_status


def test_post_with_fixture(valid_payload):
    response = requests.post(f'{BASE_URL}/posts', json=valid_payload)
    assert response.status_code == 201
    assert response.json()['title'] == valid_payload['title']


@pytest.mark.parametrize('id, expected_status', [
    (1, 200),
    (5, 200),
    (10, 200),
    (9999, 404)
])
def test_get_user(id, expected_status):
    response = requests.get(f'{BASE_URL}/users/{id}')
    assert response.status_code == expected_status


def test_create_post_with_valid_data(valid_new_post):
    response = requests.post(f'{BASE_URL}/posts', json=valid_new_post)
    assert response.status_code == 201
    assert response.json()['userID'] == 1


def test_create_post_with_no_data():
    payload = {}
    response = requests.post(f'{BASE_URL}/posts', json=payload)
    assert response.status_code == 400