nos = [5, 6, 3, 4, 1, 8]

# get a new list from nos list consisting of only the odd numbers from the nos list
# (without for comprehension, without putting any explicit loop)

# functional programming (no explicit loops)
def is_odd(element):
    return element % 2
l = filter(is_odd, nos)
print(list(l))
'''for ele in l:
    print(ele)'''

# get a new list from nos list consisting of squares of numbers from the nos list
# (without for comprehension, without putting any explicit loop)

'''def squares(element):
    return element ** 2
l2 = list(map(squares, nos))
print(l2)'''

# only if the function has only one statement (expression)
# lambda function (inline function)
l3 = list(map(lambda element: element ** 2, nos))
print(l3)

# get a new list of odd numbers greater than 1
print(list(filter(lambda element: element % 2 and element > 1, nos)))