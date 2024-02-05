# Display all the integer with sum of it's digit as even 

def sum_of_digits(integer):
    digit_sum = 0

    while integer > 0:
        digit_sum += integer % 10
        integer //= 10

    return digit_sum

def display_numbers_with_even_digit_sum(start, end):
    print(f"Integers within the range {start} to {end} with even digit sum:")

    for number in range(start, end + 1):
        if sum_of_digits(number) % 2 == 0:
            print(number)

def main():
    start_range = 100
    end_range = 200

    display_numbers_with_even_digit_sum(start_range, end_range)

if __name__ == "__main__":
    main()

