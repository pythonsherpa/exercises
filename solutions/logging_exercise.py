"""
Logging exercise
"""
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)-8s %(message)s",
)


def main():
    logging.info("Start program")
    age = ask_user_age()
    age_in_months = calculate_age_in_months(age)
    print_age(age_in_months)
    logging.info("End program")


def ask_user_age():
    logging.info("Asking user's age")
    age = int(input("What is your age in years? "))
    logging.debug(f"User answered: {age}")
    return age


def calculate_age_in_months(years):
    logging.info(f"Calculating age ({years} years)")
    return years * 12


def print_age(age_in_months):
    logging.info(f"Printing age in months {age_in_months}")
    print(f"You are {age_in_months} months old.")


if __name__ == "__main__":
    main()
