mylist = [1,2,3,"Code", (3,5,1), False, ]

if(len(mylist) < 5):
    print("List has fewer than 5 elements")
elif(5 <= len(mylist)<= 10):
    print("The list has at least 5 but at most 10 elements")
else:
    print("The list has more than 10 elements")