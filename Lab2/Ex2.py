from datetime import datetime

# Get the current year
current_year = datetime.now().year

# Prompt the user to enter their birth year
birth_year_str = input("Please enter the year you were born (as a four-digit number): ")

# Convert the input to an integer
birth_year = int(birth_year_str)

# Calculate the age
age = current_year - birth_year

# Print the result
print(f"You entered the year {birth_year}.")
print(f"Your age is {age}.")
