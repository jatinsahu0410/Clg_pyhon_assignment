# Display all multiples of 3 in the range 10 to 50 
def display_multiples_of_three(start, end):
    print(f"Multiples of 3 within the range {start} to {end}:")
    
    for number in range(start, end + 1):
        if number % 3 == 0:
            print(number)

def main():
    start_range = 10
    end_range = 50

    display_multiples_of_three(start_range, end_range)

if __name__ == "__main__":
    main()
