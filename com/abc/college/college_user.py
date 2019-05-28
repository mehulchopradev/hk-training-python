#  parent class / superclass / base class
class CollegeUser: # implicitly inherits from the 'object' built in class in python
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def get_details(self):
        return 'Name : {0}\nGender : {1}'.format(self.name, self.gender)

    # overriden from the object class
    def __str__(self):
        return 'Name : {0}\nGender : {1}'.format(self.name, self.gender)