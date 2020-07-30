from sys import exit
import random

points = 0

def level_1():
    global points
    print('\n Level one: Basic Astronomy')    

    choice = input ('How many planets are in our solar system?\n')
    if choice != '8':
        print('Wrong answer.')
    else:
        print('Great! Keep it up!')
        points += 1
        print(points, ' points')
        level_2()

def level_2():
    global points
    print('\nLevel two: Basic Biology')    

    choice = input ('Can frogs live in salt water?\n')
    if choice != 'no':
        print('Wrong answer.')
    else:
        print('Great! Keep it up!')
        points += 1
        print(points, ' points')
        level_3()

def level_3():
    global points
    print('\nLevel three: Basic Math')    

    choice = input ('The sum of three numbers is 98. The ratio of the first to the second is 2/3, and the ratio of the second to the third is 5/8. The second number is:\n')
    if choice != '30':
        print('Wrong answer.')
    else:
        print('Great! Keep it up!')
        points += 1
        print(points, ' points')

        level_4()

def level_4():
    global points
    print('\nLevel four: Basic Physics')    

    choice = input ('Light year is a unit of what?\n')
    if choice != 'time':
        print('Wrong answer.')
    else:
        print('Great! Keep it up!')
        points += 1
        print(points, ' points')

        level_5()

def level_5():
    global points    
    print('\nLevel five: Logic')    

    choice = input ('I am an odd number. Take away a letter and I become even. What number am I?\n')
    if choice != '7':
        print('Wrong answer.')
    else:
        print('Great! You finished the questions! Your score is:')
        points += 1
        print(points, ' points')


def start():
    choice = input ("Welcome! Are you ready to start? yes/no\n")
    if choice == 'yes':
        level_1()
    else:
        print(' Okay. Take your time. ')
start()