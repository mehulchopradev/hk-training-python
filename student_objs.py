from student import Student

# visualize every real world actor as an object
s1 = Student()
s2 = Student()

# associate attributes of real world actor, with the appropriate object
s1.name = 'mehul'
s1.roll = 10
s1.gender = 'm'
s1.marks = 90

s2.name = 'jane'
s2.roll = 11
s2.gender = 'f'
s2.marks = 45

'''print(s1.name)
print(s2.name)
print(s1.roll)
print(s2.roll)'''

# real world actions translating to methods called on the object
print(s1.get_details())
# Student.getDetails(s1)

print(s2.get_details())
# Student.getDetails(s2)

print(s1.get_grade()) # Student.get_grade(s1)
print(s2.get_grade()) # Student.get_grade(s2)
