def squareroot (x):
    return x**0.5

def midpoint (x1, x2):
    return (x1, x2) / 2
    
def exponent (x,y):
    return x**y

def max(x, y):
    print("Using HandyMath max function")
    return (x > y) * x + (y > x) * y

def min(x, y):
    print("Using HandyMath min function")
    return (x < y) * x + (y < x) * y