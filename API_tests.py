import requests

BASE_URL = 'https://jsonplaceholder.typicode.com'


def test_get_single_post():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200
    assert response.json()['userID'] == 1
    assert response.json()['title'] == (
        'sunt aut facere repellat provident occaecati excepturi optio '
        'reprehenderit'
    )
    assert response.json()['body'] == (
        "quia et suscipit\nsuscipit recusandae consequuntur expedita et "
        "cum\nreprehenderit molestiae ut ut quas totam\nnostrum "
        "rerum est autem sunt rem eveniet architecto")

def test_get_single_post_another_test():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == 1
    assert "title" in data