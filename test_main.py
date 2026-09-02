import pytest

from main import (multiply, is_even, reverse_string, divide,
                  is_valid_password)
from conftest import empty_cart, habit_dict


@pytest.mark.parametrize('a, b, result', [
   (3, 4, 12),
   (4, 0, 0),
   (-3, 5, -15),
   (7, 2, 14)
])
def test_multiply_two_nums(a, b, result):
   assert multiply(a, b) == result


@pytest.mark.parametrize('number, expected', [
      (4, True),
      (7, False),
      (-6, True),
      (-9, False),
      (0, True),
])
def test_is_even(number, expected):
   assert is_even(number) == expected


def test_reverse_string():
   assert reverse_string('hello') == 'olleh'


def test_reverse_empty_string():
   assert reverse_string('') == 'The string is empty!'


def test_divide_two_positive_nums():
   assert divide(10, 2) == 5


def test_divide_by_zero():
   assert divide(12, 0) == None


def test_divide_by_invalid_types():
   assert divide('5', '7') == None


@pytest.mark.parametrize('item', ['apple', 'banana', 'kiwi'])
def test_add_item_to_cart(empty_cart, item):
   empty_cart.append(item)
   assert item in empty_cart


def test_habit_streak(habit_dict):
    assert habit_dict.get('streak') == 0

@pytest.mark.parametrize('habit_name, habit_streak', [
    ('Drink water', 1),
    ('Do exercises', 3)
])
def test_add_habit(habit_name, habit_streak, habit_dict):
    habit_dict['name'] = habit_name
    habit_dict['streak'] = habit_streak

    assert habit_dict['name'] == habit_name
    assert habit_dict['streak'] == habit_streak


@pytest.mark.parametrize('password, result', [
    ('8dsjkndsl!', True),
    ('sk1d', False),
    ('asd87v6c1!', True),
    ('----', False)
])
def test_is_valid_password(password, result):
    assert is_valid_password(password) == result

