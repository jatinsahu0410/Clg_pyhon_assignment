# print all the items in a dictionary

def print_dict_items(dictionary):
    for key, value in dictionary.items():
        print(f"{key}: {value}")

def main():
    print("Print Dictionary Items")

    # Create a dictionary (you can replace this with your own dictionary)
    sample_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

    # Print all items in the dictionary
    print_dict_items(sample_dict)

if __name__ == "__main__":
    main()
