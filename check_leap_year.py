# Check wether it is leap year or not 
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def main():
    print("Leap Year Checker")

    # Get the year from the user
    year = int(input("Enter a year: "))

    # Check if the year is a leap year
    if is_leap_year(year):
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")

if __name__ == "__main__":
    main()

