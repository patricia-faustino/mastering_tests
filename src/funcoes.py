def email_is_valid(email):
    return "@" in email and "." in email

def divide(a, b):
    if b == 0:
        return None
    return a / b

def double_sum(numbers):
    return sum( x* 2 for x in numbers)