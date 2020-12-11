# import random

# player = input('Make your move: ')
# rand_num = random.randint(0,2)

# if rand_num == 0:
#     computer = "rock"
# elif rand_num == 1:
#     computer = "paper"
# else: 
#     computer = "scissors"
# print(f"computer plays: {computer}")


# if player == computer:
#     print('Tie')
# elif player == 'rock':
#     if computer == 'scissors':
#         print('player wins')
#     if computer == 'paper':
#         print('computer wins')
# elif player == 'paper':
#     if computer == 'rock':
#         print('player wins')
#     if computer == 'scissors':
#         print('computer wins')
# elif player == 'scissors':
#     if computer == 'rock':
#         print('computer wins')
#     if computer == 'paper':
#         print('player wins')

#----------Upgrade----------
import random
pcscore = 0
usscore = 0

for time in range(3):
    player = input('Make your move: ')
    rand_num = random.randint(0,2)

    if rand_num == 0:
        computer = "rock"
    elif rand_num == 1:
        computer = "paper"
    else: 
        computer = "scissors"
    print(f"computer plays: {computer}")

    if player == computer:
        print('Tie')
    elif player == 'rock':
        if computer == 'scissors':
            print('player wins')
            usscore+=1
        if computer == 'paper':
            print('computer wins')
            pcscore+=1
    elif player == 'paper':
        if computer == 'rock':
            print('player wins')
            usscore+=1
        if computer == 'scissors':
            print('computer wins')
            pcscore+=1
    elif player == 'scissors':
        if computer == 'rock':
            print('computer wins')
            pcscore+=1
        if computer == 'paper':
            print('player wins')
            usscore+=1
    print(f'pc: {pcscore} user: {usscore}')