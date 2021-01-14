"""
Refactor the program below (use a "with" statement).
"""


def main():
    text = "Explicit is better than implicit."
    write_to_file(text)


def write_to_file(text):
    file = open("exercise.txt", "w")
    file.write(text)
    file.close()


if __name__ == "__main__":
    main()
