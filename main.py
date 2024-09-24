def fibonacci_sequence(n):
    # multistring for initializing the first two numbers
    """
    Generates a Fibonacci sequence up to a given number.

    Args:
        n: The upper limit of the sequence.

    Returns:
        A list containing the Fibonacci sequence.
    """
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

if __name__ == "__main__":
    user_range = int(input("Enter the range for the Fibonacci sequence: "))
    fibonacci_series = fibonacci_sequence(user_range)
    print(f"Fibonacci sequence up to {user_range}: {fibonacci_series}")