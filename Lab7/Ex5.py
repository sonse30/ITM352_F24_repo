# Define the tuple with mixed data types
elements = ("hello", 10, "goodbye", 3, "goodnight", 5)

# Initialize a counter for strings
string_count = 0

# Iterate through each element in the tuple
for element in elements:
    # Check if the element is a string
    if isinstance(element, str):
        string_count += 1  # Increment the counter if it is a string

# Print the result
print(f"There are {string_count} strings in the tuple.")
