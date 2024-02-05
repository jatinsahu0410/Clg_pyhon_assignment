# print Fibonacci series using iteration
def fibonacci_iterative(n):
    fib_series = [0, 1]

    for i in range(2, n):
        next_term = fib_series[i - 1] + fib_series[i - 2]
        fib_series.append(next_term)

    return fib_series

def main():
    print("Fibonacci Series using Iteration")

    # Get the number of terms from the user
    n = int(input("Enter the number of terms: "))

    # Calculate and display the Fibonacci series
    result = fibonacci_iterative(n)

    print("The Fibonacci series is:", result)

if __name__ == "__main__":
    main()
