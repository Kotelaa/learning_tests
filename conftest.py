import pytest

@pytest.fixture
def empty_cart():
    return []


@pytest.fixture
def habit_dict():
    return {'name': '',
            'streak': 0}