def abc():
    i = 1 # local int object (non callable - abc)
    k = 10 # local int object (non callable - abc)
    def pqr(): # local function object (callable - pqr)
        k = 9 # k local to pqr function
        j = 2 + i + k # inner function can access the outer function variables
        return j
    print(pqr()) # 12
    print(i) # 1
    print(k) # 10

abc()

def pqr():
    print('Hello pqr')

def xyz(f):
    f() # in effect end up calling pqr()
    print('Hello xyz')

xyz(pqr) # passing a function as a parameter to another function


def func1(i):
    def func2():
        # inner function capability to access outer function values even after
        # the outer function has returned, is called as Closures
        return i ** 2
    return func2 # a function can be returned from another function

f = func1(3)
print(f()) # in effect we are calling the func2 function

