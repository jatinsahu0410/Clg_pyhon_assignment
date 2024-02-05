# Check wether a integer is multiple of 5 and 7 simultaneously
def is_multiple_of_five_and_seven(number):
    return number % 5 == 0 and number % 7 == 0

def main():
    print("Multiple of 5 and 7 Checker")

    # Get the integer from the user
    num = int(input("Enter an integer: "))

    # Check if the number is a multiple of both 5 and 7
    if is_multiple_of_five_and_seven(num):
        print(f"{num} is a multiple of both 5 and 7.")
    else:
        print(f"{num} is not a multiple of both 5 and 7.")

if __name__ == "__main__":
    main()
