# Display all the prime number in 1 to n 
def generate_primes_up_to_n(n):
    primes = []

    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)

    return primes

def main():
    print("Prime Numbers Generator")

    # Get the value of N from the user
    n = int(input("Enter the value of N: "))

    # Generate prime numbers up to N
    prime_numbers = generate_primes_up_to_n(n)

    print(f"Prime numbers up to {n}: {prime_numbers}")

if __name__ == "__main__":
    main()

