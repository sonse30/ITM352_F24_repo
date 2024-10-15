with open('./names.txt', 'r') as names_files:
    names = names_files.readlines()  # Read all lines into a list
    num_names = 0
    for name in names:
        print(name.strip())  # Print each name, removing extra newlines
        num_names += 1
print(f"There are {num_names} names")
