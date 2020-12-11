# from random import random

# def coinflip():
#     r = random()
#     if r > 0.5:
#         return 'Heads'
#     else: 
#         return 'Tails'

# print(coinflip())

#----------*args example
# def sumAllNums(*args):
#     print(args)
#     total = 0 
#     for num in args:
#         total += num
#     return total

# print(sumAllNums(1,2,3))

#----------*args example 2
# def loginCheck(*args):
#     print(args)
#     if 'Stanislav' in args and 'Iliev' in args:
#         return 'Welcome back!'
#     return 'Login credentials not recognised'

# print(loginCheck('Stanislav','Iliev'))

#----------*kwargs example 1
# def fav_colours(**kwargs):
#     for person, color in kwargs.items():
#         print(f"{person}'s favorite color is {color}")

# fav_colours(stan = 'gray', josh = 'green')
#----------*kwargs example 2
def special_greeting(**kwargs):
    if 'Stan' in kwargs and kwargs['Stan'] == 'special':
        return "You get a special greeting, Stan"
    elif 'Stan' in kwargs:
        return f"{kwargs['Stan']} Stan!"
    else:
        return "Not sure who this is..."

print(special_greeting(Stan='Hello'))
print(special_greeting(Josh='Greetings'))
print(special_greeting(Stan='special'))
