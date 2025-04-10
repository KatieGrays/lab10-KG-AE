import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def add(a, b):
    return a + b
    pass

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return b / a # raise ZeroDivisionError if a == 0

def log(a, b):
    return math.log(a,b)
    # use math library + raise ValueError
def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError as e:
        if a < 0:
            print(f'Error: {e}')

def hypotenuse(a,b):
    return math.hypot(a,b)




def exp(a, b):
    return a**b


