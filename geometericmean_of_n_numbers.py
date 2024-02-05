# Find geometeric mean of n numbers 
def calculate_geometric_mean(numbers):
    product = 1

    for num in numbers:
        product *= num

    geometric_mean = product ** (1 / len(numbers))
    return geometric_mean

def main():
    print("Geometric Mean Calculator")

    # Get the number of elements in the set
    n = int(input("Enter the number of elements: "))

    # Get the elements of the set
    numbers = []
    for i in range(n):
        element = float(input(f"Enter element {i + 1}: "))
        numbers.append(element)

    # Calculate the geometric mean
    result = calculate_geometric_mean(numbers)

    print(f"The geometric mean of the numbers is: {result:.2f}")

if __name__ == "__main__":
    main()
