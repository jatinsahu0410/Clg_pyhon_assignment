# Check either the string is palindromic or not 
def is_palindrome(s):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    s = ''.join(s.split()).lower()

    # Check if the string is equal to its reverse
    return s == s[::-1]

def main():
    print("Palindrome Checker")

    # Get the string from the user
    input_string = input("Enter a string: ")

    # Check if the string is a palindrome
    if is_palindrome(input_string):
        print(f"{input_string} is a palindrome.")
    else:
        print(f"{input_string} is not a palindrome.")

if __name__ == "__main__":
    main()

