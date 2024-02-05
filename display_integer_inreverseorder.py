# Display input integer in reverse order 
def reverse_integer(number):
    return int(str(number)[::-1])

def main():
    print("Integer Reversal Program")

    # Get the integer from the user
    num = int(input("Enter an integer: "))

    # Reverse the integer
    reversed_num = reverse_integer(num)

    # Display the reversed integer
    print(f"The reversed integer is: {reversed_num}")

if __name__ == "__main__":
    main()
