# Exercise profiling extra (running the profiler from within the program)
import cProfile

pr = cProfile.Profile()


def main():
    print("Start the program")
    pr.enable()
    result = fib(30)
    pr.disable()
    print("The result of fib(30) is:", result)
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
    pr.print_stats(sort="calls")
