# Insert a number in a list
def insert_number_at_position(lst, number, position):
    lst = lst[:position] + [number] + lst[position:]

def main():
    print("Insert a Number at a Specific Position in a List")

    # Get the list from the user
    elements = list(map(int, input("Enter space-separated elements: ").split()))

    # Get the number to insert
    number_to_insert = int(input("Enter the number to insert: "))

    # Get the position to insert the number
    position_to_insert = int(input("Enter the position to insert the number: "))

    # Insert the number at the specified position
    insert_number_at_position(elements, number_to_insert, position_to_insert)

    # Display the modified list
    print("Modified List:", elements)

if __name__ == "__main__":
    main()

