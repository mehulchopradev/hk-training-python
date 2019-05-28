class Student:
    count = 0 # class attribute

    ''' Default one
    def __init__(self):
        pass
    '''

    def __init__(self, name=None, roll=None, gender=None, marks=None):
        # constructor

        # object attributes / instance attributes
        self.name = name
        self.roll = roll
        self.gender = gender
        self.marks = marks

        # class attributes are accessed using the class name
        Student.count += 1

    # class method
    # a class method does not have self defined
    def get_min_attendance():
        return 70

    # object method
    # an object method does have self defined
    def get_details(self):
        '''return 'Name : ' + self.name + '\nRoll : ' + str(self.roll) + '\nGender : ' + self.gender \
            + 'Marks : ' + str(self.marks)'''
        '''return 'Name: {0}\nRoll: {1}\nGender: {2}\nMarks: {3}'\
                .format(self.name, self.roll, self.gender, self.marks)'''
        return 'Name: {name}\nRoll: {roll}\nGender: {gender}\nMarks: {marks}'\
                .format(name=self.name, roll=self.roll, gender=self.gender, \
                    marks=self.marks)
    
    def get_name_gender(self):
        return (self.name, self.gender)

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