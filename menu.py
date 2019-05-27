# module -> menu

# import only the module (not the functions and variables inside the module)
# import series

# imports the functions from the module and not the module
# from series import get_fibo_series, get_even_series
from com.abc.lib.series import get_even_series, get_fibo_series

import com.abc.lib.math # user defined module of python
import math # built in module

while True:
    print('1. FiboSeries\n2. Even Series\n3. Even or odd\n4. Factorial\n5. Exit')
    choice = int(input('Enter choice : '))
    if choice == 1 or choice == 2 or choice == 3 or choice == 4:
        n = int(input('Enter n : '))
    if choice == 1:
        # print(series.get_fibo_series(n))
        print(get_fibo_series(n))
    elif choice == 2:
        # print(series.get_even_series(n))
        print(get_even_series(n))
    elif choice == 3:
        print(com.abc.lib.math.is_even_odd(n))
    elif choice == 4:
        print(math.factorial(n))
    else:
        break