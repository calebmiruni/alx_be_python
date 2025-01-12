FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
def convert_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
def main():
    print("Welcome to the Temperature Conversion Tool!")
     try:
        temperature_input = input("Enter a temperature (e.g., 32 or 100): ").strip()
        unit_input = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().lower()
        temperature = float(temperature_input)
        if unit_input == 'c':
            result = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is equal to {result:.2f}°F")
        elif unit_input == 'f':
            result = convert_to_celsius(temperature)
            print(f"{temperature}°F is equal to {result:.2f}°C")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
      except ValueError:
          print("Invalid temperature. Please enter a numeric value.")
if __name__ == "__main__":
    main()
