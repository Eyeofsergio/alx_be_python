# Define the global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Implement Conversion Functions
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# User Interaction
def main():
    temperature = float(input("Enter the temperature to convert: "))

unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if unit == 'C':
    converted_temperature = convert_to_fahrenheit("temperature")
    print(f"temperature is equal to {converted_temperature}F")

elif unit == 'F':
    converted_temperature = ("convert_to_celsius temperature")
    print(f"temperature F is equal to {converted_temperature}C")

else:
    print("Invalid temperature. Please enter a numeric value.")


