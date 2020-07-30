from sys import exit

def goldroom():
    print('This room is full of gold. How much do you take?')

    choice = input('==>')
    if '0' in choice or '1' in choice:
        howmuch = int(choice)
    else:
        dead('Man learn to type a number')

    if howmuch < 50:
        print('You are not greedy, you can escape this place and go to the outside world')
        outside()
    else:
        dead('You greedy bastard')

def outside():
    print('Sweet freedom!')
    exit()#so that it doesn`t wait for a prompt at the end when game is finished


def bearroom():
    print('there is a bear here')
    print('the bear has a bunch of honey')
    print('the bear is infront of the door')
    print('how are you going to move the bear?')
    bearmove = False

    while True:
        choice = input('==>')

        if choice == 'take honey':
            dead('the bear rips your insides out')
        elif choice == 'taunt bear' and not bearmove:
            print('the bear has moved from the door')
            print('you can go through it now')
            bearmove = True
        elif choice == 'taunt bear' and bearmove:
            dead('the bear is not impressed and bites your arm off')
        elif choice == 'open door' and bearmove:
            goldroom()
        else:
            print('I got not idea what that means')


def cthulu_room():
    print('Here you see the old one')
    print('And you go insane')
    print('Do you flee or eat your head?')

    choice = input('==>')

    if 'flee' in choice:
        start()
    elif 'head' in choice:
        dead('well that happened')
    else:
        chtulu_room()

def dead(why):
    print(why, 'good job!')
    exit(0)

def start():
    print('you are in a dark room\n there is a door you your right and left')
    print('which one do you take?')

    choice = input('==>')

    if choice == 'left':
        bearroom()
    elif choice == 'right':
        cthulu_room()
    else:
        dead('You die of starvation')

start()
