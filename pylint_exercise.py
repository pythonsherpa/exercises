"""
This is an exercise to get familiar with Pylint. 

You can install pylint with:

pip install pylint

Documentation: https://www.pylint.org

To use pylint, run the following in the terminal/commandline:
pylint pylint_exercise.py

To get help, run the following in the terminal/commandline:
pylint --help-msg=unused-variable

To suppress warnings, run the following in the terminal/commandline:
pylint exercise_3_pylint.py --disable=missing-function-docstring

Extra challenge 1:
Check out the plugin for PyCharm: https://github.com/leinardi/pylint-pycharm

Extra challenge 2:
Create a '.pylintrc' file with your own configuration
pylint --generate-rcfile > .pylintrc

Extra challenge 3:
Check out Flake8: https://flake8.pycqa.org/en/latest/
Which one do you prefer, pylint or flake8?
"""

import statistics


def main():
   name = input("What is your name? ")
   greet(name)


def greet(name):
    local_variable = 42
    print(f"Hello {name}, how are you?");
    return


if __name__ == "__main__":
    main()
