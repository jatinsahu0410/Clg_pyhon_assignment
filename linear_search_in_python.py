# Linear search 
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index if target is found
    return -1  # Return -1 if target is not found

def main():
    print("Linear Search in Python")

    # Get the list from the user
    elements = list(map(int, input("Enter space-separated elements: ").split()))

    # Get the target element to search
    target_element = int(input("Enter the element to search: "))

    # Perform linear search
    result = linear_search(elements, target_element)

    # Display the result
    if result != -1:
        print(f"{target_element} found at index {result}.")
    else:
        print(f"{target_element} not found in the list.")

if __name__ == "__main__":
    main()
