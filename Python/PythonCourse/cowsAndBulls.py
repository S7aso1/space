import random

def generate_secret():
    l = random.sample('1234567890',k=4)
    if l[0] == '0':
        return generate_secret()
    secret = ''.join(l)
    return secret


def get_user_guess():
    while True:
        guess = input('Enter a 4 digit number : ')
        if len(guess) == 4 and guess[0] != '0' and guess.isdigit() and len(set(guess))==4:
            return guess
        else:
            print(f'{guess} is not a valid input')
        
def match_numbers(secret,guess):
    assert len(guess) == 4
    bulls = 0
    cows = 0
    for n in range (0,4):
        char = guess[n]
        i = secret.find(char)
        if i == n:
            bulls +=1
        elif i!=-1:
            cows +=1
    return bulls,cows
tries = 0
secret = generate_secret()
print(secret)
while True:
    guess = get_user_guess()
    bulls,cows = match_numbers(secret,guess)
    print('Bulls : ' + str(bulls) + ' Cows : ' + str(cows))
    tries += 1
    if bulls<4:
        print (tries)
    else:
        print ('Correct! It took you ' + str(tries) + ' attempts to guess the secret')
        break




