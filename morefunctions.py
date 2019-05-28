# 0 to n parameters
def myadd(*nos): # positional argument packing
    # nos is treated as a tuple inside this function
    return sum(nos)

# positional arguments passed to the function will be packed in a tuple inside the function
print(myadd())
print(myadd(1))
print(myadd(5, 6, 3))
print(myadd(5, 7, 9, 10, 34, 23))

def perimeter(length, breadth):
    return 2 * (length + breadth)

stats = [9, 4]
print(perimeter(stats[0], stats[1]))
print(perimeter(*stats)) # positional argument unpacking


def area(**s):
    # print(s) # dictionary
    return s['length'] * s['breadth']

# print(area(6.1, 5.9))
# keyword arguments packing
print(area(length=6.1, breadth=5.9))
print(area(breadth=5, length=8))
# print(area(l=4, b = 3)) # error as keyword argument will not be found in dictionary


stats_map = {'breadth': 5, 'length': 6}
print(perimeter(stats_map['length'], stats_map['breadth']))
print(perimeter(**stats_map)) # dictionary unpacking to keyword arguments