from student import Student

s1 = Student()
'''
1. create an object in ram - 7007
2. Student.__init__(7007)
'''

s1.name = 'mehul'
s1.roll = 11
s1.gender = 'm'
s1.marks = 90

s2 = Student('jane', 10, 'f', 87)
'''
1 Create an object in ram - 7009
2 Student.__init__(7009, 'jane', 10, 'f', 87)
'''

'''s2.name = 'jane'
s2.roll = 10
s2.gender = 'f'
s2.marks = 87'''

s3 = Student(name='jill', roll=20, gender='f', marks=46)
'''s3.name = 'jill'
s3.roll = 20
s3.gender = 'f'
s3.marks = 46'''

slist = [s1, s2, s3]
smap = {11: s1, 10: s2, 20: s3}
search = int(input('Enter roll : '))

'''for student in slist:
    if student.roll == search:
        print(student.get_details())
        break
else:
    # will execute if the corresponding for block is exhausted i.e. no break in the for
    print('Not found')'''

if search in smap:
    student = smap[search]
    print(student.get_details())
else:
    print('Not found')
