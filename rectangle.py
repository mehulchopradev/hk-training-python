length = float(input('Enter length : '))
breadth = float(input('Enter breadth : '))

def area(length, breadth):
    return length * breadth

def perimeter(length, breadth):
    return 2 * (length + breadth)

p = perimeter(length, breadth)
a = area(length, breadth)

print(p)
print(a)