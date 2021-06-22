"""
Refactor the 'calculate_tax' function. Create a new
function for calculating the discount.

If you use PyCharm, use the "Extract Method" functionality.

Example from:
https://www.jetbrains.com/help/pycharm/extract-method.html
"""
from enum import Enum


class Category(Enum):
    A = 1
    B = 2
    C = 3


def calculate_tax(category, income):
    if category == Category.A:
        discount = 10
    elif category == Category.B:
        discount = 5
    else:
        discount = 0
    return income * (100 - discount) / 100
