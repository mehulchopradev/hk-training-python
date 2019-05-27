class Student:

    def get_details(self):
        return 'Name : ' + self.name + '\nRoll : ' + str(self.roll) + '\nGender : ' + self.gender \
            + 'Marks : ' + str(self.marks)

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