import os

file_path = './names.txt'  # Change to 'names.txt' to test a valid file
    
# Check if the file exists and is readable before opening it
if os.path.exists(file_path) and os.access(file_path, os.R_OK):
    try:
        with open(file_path, 'r') as names_files:
            names = names_files.readlines()  # Read all lines into a list
            num_names = 0
            for name in names:
                print(name.strip())  # Print each name, removing extra newlines
                num_names += 1
        print(f"There are {num_names} names")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
else:
    print(f"Error: The file '{file_path}' does not exist or is not readable.")
file_path = './names.txt'
