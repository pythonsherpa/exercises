# Exercise profiling
def main():
    print("Start the program")
    print("The result of fib(30) is:", fib(30))
    print("End the program")


def fib(n):
    """
    Recursive implementation
    of the Fibonacci Sequence
    """
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    main()
