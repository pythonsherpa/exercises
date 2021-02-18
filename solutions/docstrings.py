"""
Add 'docstrings' to the following functions and classes.
Make sure to follow the Python conventions.
"""


# 1
def square(n):
    """Return the square of n."""
    return n * n


# 2
def count_vowels(word):
    """Return the total number of vowels."""
    number_of_vowels = 0
    for char in word.lower():
        if char in "aeiou":
            number_of_vowels += 1
    return number_of_vowels


# 2
class Dog:
    """A class to represent a dog."""

    def __init__(self, name):
        self.name = name

    def bark(self):
        """Make the dog bark."""
        print(f"{self.name} says whoof!")