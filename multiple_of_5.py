# Check wether the integer is multiple of five or not
def is_multiple_of_five(number):
    return number % 5 == 0

def main():
    print("Multiple of 5 Checker")

    # Get the integer from the user
    num = int(input("Enter an integer: "))

    # Check if the number is a multiple of 5
    if is_multiple_of_five(num):
        print(f"{num} is a multiple of 5.")
    else:
        print(f"{num} is not a multiple of 5.")

if __name__ == "__main__":
    main()

