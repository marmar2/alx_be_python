CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

def convert_to_celsius(fahrenheit):
    tempInC = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return tempInC
def convert_to_fahrenheit(celsius):
    tempInf = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return tempInf


Temp = input("Enter the temperature to convert: ")
try:
    Temperature = float(Temp)
except ValueError:
    raise ValueError("Invalid temperature. Please enter a numeric value.")


unit = input("Is this temperature in Celsius or Fahrenheit? (C/F):")

if unit == "C":
    print(f"{Temp}°C is {convert_to_fahrenheit(float(Temp))} °F")
elif unit == "F":
    print(f"{Temp}°F is {convert_to_celsius(float(Temp))} °C")  