from main import multiply, is_even, reverse_string, divide


def test_multiply_two_nums():
   assert multiply(3, 4) == 12


def test_is_even_with_even_num():
   assert is_even(4) == True


def test_is_even_with_odd_num():
   assert is_even(7) == False


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

