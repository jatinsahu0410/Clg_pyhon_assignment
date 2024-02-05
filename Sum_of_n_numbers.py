# Sum of n numbers using list
def sum_of_numbers(numbers):
    return sum(numbers)

def main():
    print("Sum of N Numbers using a List")

    # Get the value of N from the user
    n = int(input("Enter the value of N: "))

    # Get the N numbers from the user
    numbers = [float(input(f"Enter number {i + 1}: ")) for i in range(n)]

    # Display the sum of the numbers
    result = sum_of_numbers(numbers)
    print(f"The sum of the numbers is: {result}")

if __name__ == "__main__":
    main()
