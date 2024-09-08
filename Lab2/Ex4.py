#Ask user to input a number using stdin
number = float(input("enter a decimal formatted number between 1 and 100: "))
#Print out the square of the input that is rounded 2 decimal places
number_squared = round(number **2,2)
print("The square of "+ str(number) +" is " + str(pow(number_squared)))