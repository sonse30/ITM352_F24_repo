with open('./names.txt', 'r') as names_files:
   names = names_files.read()
lines = names.split('\n')
print(f"{names}\n There are {len(lines)} names ")
