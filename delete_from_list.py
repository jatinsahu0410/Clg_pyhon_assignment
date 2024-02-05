# delete an element from a list by index
def delete_element_by_index(lst, index):
    if 0 <= index < len(lst):
        lst.pop(index)
        print(f"Element at index {index} deleted.")
    else:
        print("Invalid index. Please enter a valid index.")

def main():
    print("Delete an Element from a List by Index")

    # Get the list from the user
    elements = list(map(int, input("Enter space-separated elements: ").split()))

    # Get the index to delete
    index_to_delete = int(input("Enter the index to delete: "))

    # Delete the element at the specified index
    delete_element_by_index(elements, index_to_delete)

    # Display the modified list
    print("Modified List:", elements)

if __name__ == "__main__":
    main()

