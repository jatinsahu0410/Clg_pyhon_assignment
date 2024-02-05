# print the numbers from a given number n till 0 using recursion
def print_numbers_from_n_to_zero(n):
    if n >= 0:
        print(n)
        print_numbers_from_n_to_zero(n - 1)

def main():
    print("Print Numbers from N to 0 using Recursion")

    # Get the value of N from the user
    n = int(input("Enter the value of N: "))

    # Print numbers from N to 0 using recursion
    print_numbers_from_n_to_zero(n)

if __name__ == "__main__":
    main()
