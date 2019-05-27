name = input('Enter name : ')
roll = int(input('Enter roll : '))
gender = input('Enter gender : ')
marks = float(input('Enter marks : '))

def get_details(name, roll, gender, marks):
    return 'Name : ' + name + '\nRoll : ' + str(roll) + '\nGender : ' + gender \
        + 'Marks : ' + str(marks)

def calc_grade(marks):
    grade = ''
    if marks > 100 or marks < 0:
        grade = 'I'
    elif marks >= 70:
        grade = 'A'
    elif marks >= 60:
        grade = 'B'
    elif marks >= 40:
        grade = 'C'
    else:
        grade = 'F'
    return grade

print(get_details(name, roll, gender, marks))
print(calc_grade(marks))