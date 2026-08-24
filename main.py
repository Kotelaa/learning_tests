def multiply(a, b):
    return a * b

def is_even(num):
   return num % 2 == 0


def reverse_string(s):
   if s == '':
       return 'The string is empty!'
   return s[::-1]


def divide(a, b):
   try:
       result = a / b
   except ZeroDivisionError:
       print ('You can not divide by zero!')
       return None
   except (TypeError, ValueError) as e:
       print(f'Invalid types: {e}')
       return None
   return result


def is_valid_password(password):
    if len(password) < 8:
        return False
    return True