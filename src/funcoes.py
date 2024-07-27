import time

def email_is_valid(email):
    return "@" in email and "." in email

def divide(a, b):
    if b == 0:
        return None
    return a / b

def division_with_treatment(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b

def double_sum(numbers):
    return sum( x* 2 for x in numbers)

def sum_numbers(a, b):
    return a + b

def fatorial(n):
    if not isinstance(n, int) or n < 0:
        raise TypeError("O argumento deve ser um número inteiro e positivo")
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)
    
def slow_sum(a,b):
    time.sleep(2)
    return a + b

def multiply(a, b):
    return a * b