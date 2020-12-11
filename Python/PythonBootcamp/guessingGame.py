import random

computerNum = random.randint(1,11)
num = input('guess a number in range 1 - 10: ')
num = int(num)

while num != computerNum:
    if num > computerNum: 
        print('too high')
    else: 
        print('too low')
    num = input('try again ')
    num = int(num)

print('you got it')

