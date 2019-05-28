from com.abc.college.student import Student
from com.abc.college.professor import Professor

s = Student(name='mehul', gender='m', roll=10, marks=90)
p = Professor(name='jane', gender='f')
i = 3
name = 'mehul'

print(name)
print(i)
print(s)
print(p)

'''print(s.name)
print(s.gender)

print(p.name)
print(p.gender)'''

# print(s.get_details()) # calls the overriden method
# print(p.get_details()) # call the inherited method
