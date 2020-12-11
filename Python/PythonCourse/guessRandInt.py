import random

computerNum = random.randint(1,9)
num = input('guess a number in range 1 - 9: ')
num = int(num)
attempts = 0

while num != computerNum:
    if num > computerNum: 
        print('too high')
        attempts += 1
    else: 
        print('too low')
        attempts += 1
    num = input('try again ')
    num = int(num)

print(f'you got it. it took you {attempts} attempts.')

