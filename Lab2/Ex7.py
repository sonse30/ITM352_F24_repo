# Prompt the user to enter a temperature in Fahrenheit
fahrenheit = input("Enter the temperature in Fahrenheit: ")

# Convert the input value from string to float
fahrenheit_float = float(fahrenheit)

# Conversion formula from Fahrenheit to Celsius
celsius = (fahrenheit_float - 32) * (5 / 9)

# Print the results
print(f"You entered a temperature of {fahrenheit_float:.2f}°F.")
print(f"Equivalent temperature in Celsius is {celsius:.2f}°C.")