# s = input('enter a number: ')

# try: 
#     print()
#     n = int(s)
#     x = 7 / num
# except ZeroDivisionError:
#     print('cant divide by 0')
# except ValueError:
#     print('this is not a number')
# else: 
#     print(f'7 / {n} = {x}')
# finally:
#     print('this will always be printed')

# import io

# f = open('test.txt', 'w')
# try: 
#     print(pdk141)
#     f.write('TEST')
# except io.UnsupportedOperation as e:
#     print(e)
#     print(type(e))
#     print('this is unsupported operation')
# finally:
#     f.close()



#creating our own error
import io
from math import sqrt

class myStupidError(Exception):

def stupidFunc(n):
    if n < 0:
        raise myStupidError
    return sqrt(n)

n = int(input('enter a number'))
try: 
    print(stupidFunc(num))
except myStupidError:
    print('a stupid error occured')

