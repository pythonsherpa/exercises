"""
This is an exercise to get familiar with Pylint.
You can install pylint with:
pip install pylint
To use pylint, run the following in the terminal/commandline:
pylint pylint_exercise.py
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
