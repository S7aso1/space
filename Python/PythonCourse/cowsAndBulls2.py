import random

number = []
attempt = 0

def makeNumber(): #makes a list with no repeats
    for i in range(4):
        x = random.randrange(0,10)
        number.append(x)

    if len(number) > len(set(number)):
        number.clear()
        makeNumber()

def playGame():
    global attempt
    attempt += 1
    cows = 0
    bulls = 0
    print(number)
    choice = input('please enter 4 digit number ')
    guess = []
    for i in range (4):
        guess.append(int(choice[i]))

    for j in range (4):
        for x in range (4):
            if(guess[j] == number[x]):
                cows += 1

    for x in range (4):
        if guess[x] == number[x]:
            bulls += 1

    print(f'Bulls: {bulls}')
    print(f'Cows: {cows}')

    if(bulls == 4):
        print(f'you wont after {attempt} attempts')
    elif (bulls != 4):
        playGame()
makeNumber()
playGame()