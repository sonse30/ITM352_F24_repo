mylist = [
    [1,2,3,"Code", (3,5,1), False, ], #More than 5 elements but less than 10
    [1,2,3], #Less than 5 elements,
    [1,2,3,4,5,6,7,8,"code",11,23,31,41,1551,16661,111,33231] #Greater than 10 elements
]

mylist = mylist[2]
if(len(mylist) < 5):
    print("List has fewer than 5 elements")
elif(5 <= len(mylist)<= 10):
    print("The list has at least 5 but at most 10 elements")
else:
    print("The list has more than 10 elements")