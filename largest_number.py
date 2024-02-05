# Largest number in a list 
def find_largest_number(arr):
    if not arr:
        return None  # Return None for an empty list

    largest_number = arr[0]

    for num in arr:
        if num > largest_number:
            largest_number = num

    return largest_number

def main():
    print("Find the Largest Number in a List")

    # Get the list from the user
    elements = list(map(int, input("Enter space-separated elements: ").split()))

    # Find and display the largest number
    largest_number = find_largest_number(elements)

    if largest_number is not None:
        print(f"The largest number in the list is: {largest_number}")
    else:
        print("The list is empty.")

if __name__ == "__main__":
    main()
