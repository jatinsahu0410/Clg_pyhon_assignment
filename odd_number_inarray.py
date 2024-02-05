# find the odd numbers in an array
def find_odd_numbers(arr):
    odd_numbers = [num for num in arr if num % 2 != 0]
    return odd_numbers

def main():
    print("Find Odd Numbers in an Array")

    # Get the array from the user
    elements = list(map(int, input("Enter space-separated elements: ").split()))

    # Find and display the odd numbers
    odd_numbers = find_odd_numbers(elements)
    
    if odd_numbers:
        print("Odd numbers in the array:", odd_numbers)
    else:
        print("No odd numbers found in the array.")

if __name__ == "__main__":
    main()
