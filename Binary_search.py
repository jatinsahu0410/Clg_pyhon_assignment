# Binary Search in sorted list 
def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid  # Return the index if target is found
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Return -1 if target is not found

def main():
    print("Binary Search in Python")

    # Get a sorted list from the user
    elements = sorted(list(map(int, input("Enter space-separated sorted elements: ").split())))

    # Get the target element to search
    target_element = int(input("Enter the element to search: "))

    # Perform binary search
    result = binary_search(elements, target_element)

    # Display the result
    if result != -1:
        print(f"{target_element} found at index {result}.")
    else:
        print(f"{target_element} not found in the list.")

if __name__ == "__main__":
    main()
