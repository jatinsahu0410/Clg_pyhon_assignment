# Find factorial using rec in python 
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    print("Factorial Calculator using Recursion")

    # Get the value of N from the user
    n = int(input("Enter a non-negative integer: "))

    # Check if the input is non-negative
    if n < 0:
        print("Please enter a non-negative integer.")
    else:
        # Calculate and display the factorial
        result = factorial(n)
        print(f"The factorial of {n} is: {result}")

if __name__ == "__main__":
    main()
