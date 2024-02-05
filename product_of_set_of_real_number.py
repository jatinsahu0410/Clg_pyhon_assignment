def calculate_product(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

def main():
    print("Product of a Set of Real Numbers Calculator")

    # Get the number of elements in the set
    n = int(input("Enter the number of elements in the set: "))

    # Get the elements of the set
    numbers = []
    for i in range(n):
        element = float(input(f"Enter element {i + 1}: "))
        numbers.append(element)

    # Calculate the product
    result = calculate_product(numbers)

    print(f"The product of the set is: {result:.2f}")

if __name__ == "__main__":
    main()
