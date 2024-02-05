# WAP to convert temp from degree centigrade to fahernheit

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def main():
       
    celsius = float(input("Enter temperature in Celsius: "))
    result = celsius_to_fahrenheit(celsius)
    print(f"{celsius} Celsius is equal to {result:.2f} Fahrenheit")
if __name__ == "__main__":
    main()
