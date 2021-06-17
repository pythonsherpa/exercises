"""
Rename the following variables and function names
"""


def rename_variables_in_this_function():
    # 1 - descriptive name
    first_name = input("What is your first name? ")

    # 2 - snake_case
    last_name = "Johnson"

    # 3 - snake_case (could even be just "movie")
    movie_title = "Pulp Fiction"

    # 4 - descriptive name
    operating_systems = ["Windows", "Linux", "MacOS"]

    # 5 - no abbreviations
    actors = ["Tom Hanks", "Brad Pitt", "Johnny Depp"]

    # 6 - type can be inferred
    fruits = ["apple", "banana", "kiwi", "orange"]

    # 7 - type can be inferred
    grades = {"English": 90, "Biology": 80, "Math": 100}


# Rename this function and its variables
def convert_temperature(celsius):
    """Return temperature converted from Celsius to Fahrenheit"""
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit


# Rename this class -> PascalCase
class ElectricVehicle:

    def __init__(self, brand, battery):
        self.brand = brand
        self.battery = battery
