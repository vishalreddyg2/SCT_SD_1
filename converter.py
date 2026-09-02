def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15
def main():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")

    choice = input("Choose an option (1-4): ")
    value = float(input("Enter the temperature value: "))

    if choice == "1":
        result = celsius_to_fahrenheit(value)
        print(f"{value}°C = {result}°F")
    elif choice == "2":
        result = fahrenheit_to_celsius(value)
        print(f"{value}°F = {result}°C")
    elif choice == "3":
        result = celsius_to_kelvin(value)
        print(f"{value}°C = {result}K")
    elif choice == "4":
        result = kelvin_to_celsius(value)
        print(f"{value}K = {result}°C")
    else:
        print("Invalid choice.")

main()