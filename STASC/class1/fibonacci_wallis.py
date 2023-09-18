def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

def wallis(n):
    result = 2.0  # Initialize the result with 2.0
    for i in range(1, n + 1):
        numerator = 4.0 * (i ** 2)
        denominator = numerator - 1
        result *= numerator / denominator
    return result


if __name__ == '__main__':
    fibonacci(n)