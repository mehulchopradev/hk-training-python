l = 5 # module level
b = 3 # module

def area():
    return l * b # accessing module level variables

def perimeter():
    # a variable is created in python when u give a value to it
    l = 4 # local to the function
    b = 3 # local to the function
    if b > 2:
        c = 9
    return 2 * (l + b)

print(area())
print(perimeter())
print(l) # module - 5
print(b) # module - 3