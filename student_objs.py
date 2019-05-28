from student import Student

# access the class attribute using the class name
print(Student.count) # 0
# visualize every real world actor as an object
s1 = Student()
s2 = Student()

print(Student.count) # 2

# associate attributes of real world actor, with the appropriate object
s1.name = 'mehul'
s1.roll = 10
s1.gender = 'm'
s1.marks = 90

s2.name = 'jane'
s2.roll = 11
s2.gender = 'f'
s2.marks = 45

t1 = s1.get_name_gender()
print('Name ' + t1[0])
print('Gender ' + t1[1])

# pythonic!!
name, gender = s2.get_name_gender() # tuple unpacking
print('Name : ' + name)
print('Gender : ' + gender)

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

# class methods are called using the class name. They are independent of any Student object created
print(Student.get_min_attendance()) # Student.get_min_attendance()