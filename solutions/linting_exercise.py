"""
This is an exercise to get familiar with ruff.

You can install ruff with:
pip install ruff

To use ruff, run the following in the terminal/commandline:
ruff check linting_exercise.py
"""


def main():
    """Run the program."""
    name = input("What is your name? ")
    greet(name)


def greet(name):
    """Return a full sentence greeting."""
    return f"Hello {name}, how are you?"


def make_percentage(number):
    """Return the number as a percentage."""
    percentage = number / 100
    return f"{percentage}%"


if __name__ == "__main__":
    main()
