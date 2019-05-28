nos = [5, 6, 3, 4, 7, 10, 1, 3]

# print all the even numbers from the list
for n in nos:
    if not n % 2:
        print(n)

# get a new list which is the odd nos from the nos list (filter)
'''odds = []
for n in nos:
    if n % 2:
        odds.append(n)'''
# for comprehensions
odds = [n for n in nos if n % 2]
print(odds)

# get a new list which is squares of element from the nos list (mapping)
'''squares = []
for n in nos:
    squares.append(n ** 2)'''
# for comprehensions
squares = [n ** 2 for n in nos]
print(squares)

# get a new list which has squares of even elements greater than 2 from nos list
e = [n ** 2 for n in nos if not n % 2 and n > 2]
print(e)