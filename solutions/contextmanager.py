"""
Refactor the program below (use a "with" statement).
"""


def main():
    text = "Explicit is better than implicit."
    write_to_file(text)


def write_to_file(text):
    with open("exercise.txt", "w") as f:
        f.write(text)


if __name__ == "__main__":
    main()
