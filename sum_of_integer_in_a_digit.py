# Sum of all the digits of a integer 
def sum_of_digits(integer):
    # Make sure the input is positive
    integer = abs(integer)
    
    # Initialize sum and iterator
    digit_sum = 0
    current_number = integer

    # Calculate sum of digits using a while loop
    while current_number > 0:
        digit = current_number % 10
        digit_sum += digit
        current_number //= 10

    return digit_sum

def main():
    print("Sum of Digits Calculator")

    # Get the integer from the user
    num = int(input("Enter an integer: "))

    # Calculate the sum of digits
    result = sum_of_digits(num)

    print(f"The sum of the digits is: {result}")

if __name__ == "__main__":
    main()
