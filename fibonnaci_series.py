# N th term in fibonnaci series 
def fibonacci_recursive(n):
    if n <= 0:
        return "Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def main():
    print("Fibonacci Series using Recursion")

    # Get the value of N from the user
    n = int(input("Enter the value of N: "))

    # Calculate and display the Nth term in the Fibonacci series
    result = fibonacci_recursive(n)

    print(f"The {n}th term in the Fibonacci series is: {result}")

if __name__ == "__main__":
    main()
