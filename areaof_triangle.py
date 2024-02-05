# area of triangle who's all sides are given 

import math

def calculate_area_of_triangle(side1, side2, side3):
    # Calculate semi-perimeter
    s = (side1 + side2 + side3) / 2

    # Calculate area using Heron's formula
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    return area

def main():
    print("Triangle Area Calculator")
    side1 = float(input("Enter length of side 1: "))
    side2 = float(input("Enter length of side 2: "))
    side3 = float(input("Enter length of side 3: "))

    if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
        area = calculate_area_of_triangle(side1, side2, side3)
        print(f"The area of the triangle is: {area:.2f} ")
    else:
        print("These side lengths do not form a valid triangle.")

if __name__ == "__main__":
    main()

