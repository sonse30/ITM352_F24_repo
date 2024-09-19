first_name = input("First name: ")
middle_name = input ("Middle name; ")
last_name = input ("Last name: ")


#Exercise 1A
full_name = first_name + " " + middle_name[0] + ". " + last_name

#Exercise 1B
full_name = f"{first_name} {middle_name[0]}. {last_name}"

#Exercise 1C
full_name = "%s %s. %s" %(first_name, middle_name[0], last_name)

#Exerice 1D
full_name = "{} {}. {}".format(first_name, middle_name[0], last_name)

#Exercise 1E
fullname = [first_name, middle_name[0] + ".", last_name]
full_name = " ".join(fullname)

print (full_name)

