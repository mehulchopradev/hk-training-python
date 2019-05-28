# dot indicates current directory
# we do this since both modules are in a package
# rather than writing full package name from com , we write only relative path
from .college_user import CollegeUser

# child class / subclass / concrete class
class Student(CollegeUser):
    def __init__(self, name, gender, roll, marks):
        super().__init__(name, gender)

        self.roll = roll
        self.marks = marks

    # method overriding
    # signature of the overriden function and super class function must be the same
    def get_details(self):
        part1 = super().get_details() # super class get_details method
        return '{0}\nRoll : {1}\nMarks : {2}'\
            .format(part1, self.roll, self.marks)

    def get_grade(self):
        grade = ''
        marks = self.marks

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