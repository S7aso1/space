from sys import exit
import random


def room1():
    print('You have found a room with three doors: Left, Middle and  Right')

    choice = input ('Where do you want to go?')
    if choice == 'left':
        room3()
    elif choice == 'right':
        room2()
    elif choice == 'middle':
        room5()
    else:
        print('You must pick one of the three')

def room2():
    print('You have found a room with three doors: Left, Middle and  Right')

    choice = input ('Where do you want to go?')
    if choice == 'left':
        room1()
    elif choice == 'right':
        room4()
    elif choice == 'middle':
        room5()
    else:
        print('You must pick one of the three')

def room3():
    print('You enter a dark room. You can light a torch or go back')

    choice = input('Do you wish to light a torch or go back?')
    if choice == 'go back':
        print('You have returned to the previous room')
        room1()
    elif choice == 'light torch':
        print('You got attacked by Pinwheel.')

        doroll = input('Roll to see if you survive.')
        if doroll == 'roll':
            for num in range(100):
                print (random.randrange(1,101))


    else:
        print('You must make a choice.')

def room4():
    print('You have found a room with a portal')

    choice = input('Take it?')
    if choice == 'yes':
        print('You went through it and now you are in another room')
        room6()
    elif choice == input():
        print('You are still in the same room')
    else:
        print('You must make a decision...')

def room5():
    print('You are now in a room with two doors: Left and right, pick one')

    choice = input('Left or right?')

    if choice == 'left':
        room6()
    if choice == 'right':
        room7()

def room6():
    print('You are in a room with a portal inside and a door.')

    choice = input('Choose portal or door')

    if choice == 'portal':
        room4()
    if choice == 'door':
        broom()

def room7():
    print('You are now in a room with two doors: Left and right, pick one')

    choice = input('Left or right?')

    if choice == 'left':
        room5()
    if choice == 'right':
        broom()

def broom():
    print('You enter a room and you trigger a trap')
    print('Pick your lucky number to see if you dodge the trap')

    choice = int(input('Lucky number'))

    if choice > 100:
        print('You survive! the game')

    elif choice < 100:
        print('Death by arrow to the knee')

    else:
        print('Pick a number!')

def start(): #if start function is on top of code it wont work cuz it wont find room 1 and 2
    print('This is the start')
    print('You have two doors: Left and Right')

    choice = input ('Where do you want to go?')
    if choice == 'left':
        room1()
    elif choice == 'right':
        room2()
    else:
        print('You must pick a door ')


start()
