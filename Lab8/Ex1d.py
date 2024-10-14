with open('./names.txt', 'r') as names_files:
    names = names_files.readline()  # Start by reading the first line
    num_names = 0
    while names != '':
        print(names.strip())  # Print the name, removing any extra newlines
        num_names += 1
        names = names_files.readline()  # Read the next line
        
print(f"There are {num_names} names")
