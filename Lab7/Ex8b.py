# Initial tuple
my_tuple = (1980, 1982, 1983)

try:
    my_tuple.append(1984)  
except AttributeError:
    print("An attempt was made to append a value to the tuple, which is not allowed.")
