def apply_function(x, y, func):
    return f"The function {func.__name__} applied to {x}, {y} = {func(x, y)}"

# Example usage:
print(apply_function(5, 3, max))  # "The function max applied to 5, 3 = 5"
