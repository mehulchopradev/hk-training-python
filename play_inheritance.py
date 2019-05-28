# vendor 1
class Abc:
    def fun(self):
        print('Fun of Abc')

    def show(self):
        print('Show of Abc')

# vendor 2
class Xyz:
    def fun(self):
        print('Fun of Xyz')

    def hello(self):
        print('Hello')

class MyOwnClass(Abc, Xyz): # multiple inheritance
    # MRO (Method resolution order)
    def fun(self):
        super().fun() # Fun of Abc
        Xyz.fun(self) # Fun of Xyz

m = MyOwnClass()
m.hello()
m.fun()
