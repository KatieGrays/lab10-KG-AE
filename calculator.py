import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

# Make DivisionError
def div(a, b):
    return a / b
try:
    a = 10
    b = 0
    result = a/b
except ZeroDivisionError as e:
    print(f"Error: {e}")

def log(a, b):
    if a <= 0 or a == 1:
        raise ValueError(f"Error: {a}")
    if b <= 0:
        raise ValueError(f"Error: {b}")

    return math.log(a, b)
# Make value error

def exp(a, b):
    return a ** b

