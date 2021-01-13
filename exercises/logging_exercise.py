"""
Logging exercise
"""


def main():
    age = ask_user_age()
    age_in_months = calculate_age_in_months(age)
    print_age(age_in_months)


def ask_user_age():
    age = int(input("What is your age in years? "))
    return age


def calculate_age_in_months(years):
    return years * 12


def print_age(age_in_months):
    print(f"You are {age_in_months} months old.")


if __name__ == "__main__":
    main()
