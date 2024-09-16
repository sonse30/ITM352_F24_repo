from HandyMath import midpoint, squareroot, exponent, max, min

# Input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"Midpoint: {midpoint(num1, num2)}")
print(f"Square root of {num1} squared: {squareroot(num1**2)}")
print(f"{num1} raised to the power of {num2}: {exponent(num1, num2)}")
print(f"Max of {num1} and {num2}: {max(num1, num2)}")
print(f"Min of {num1} and {num2}: {min(num1, num2)}")
