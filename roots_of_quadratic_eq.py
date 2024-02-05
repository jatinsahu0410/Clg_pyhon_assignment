# Find the roots of quadratic equation
import cmath  # Importing cmath for complex number support

def find_roots(a, b, c):
    # Calculate the discriminant
    delta = cmath.sqrt(b**2 - 4*a*c)

    # Calculate the roots using the quadratic formula
    root1 = (-b + delta) / (2*a)
    root2 = (-b - delta) / (2*a)

    return root1, root2

def main():
    print("Quadratic Equation Root Finder")

    # Get coefficients from the user
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    # Find and display the roots
    roots = find_roots(a, b, c)

    print(f"The roots of the quadratic equation are: {roots}")

if __name__ == "__main__":
    main()
