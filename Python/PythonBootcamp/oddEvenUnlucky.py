# top = input('what is the top of the range? ')
# top = int(top)

# for num in range (1, top+1):
#     if num == 4 or num == 13:
#         print(f'{num} is unlucky')
#     elif (num % 2) == 0:
#         print(f"{num} is even")
#     else:
#         print(f'{num} is odd')

#-------Better version-------#
top = input('what is the top of the range? ')
top = int(top)

for num in range (1, top+1):
    if num == 4 or num == 13:
        state = 'unlucky'
    elif (num % 2) == 0:
        state = 'even'
    else:
        state = 'odd'

    print(f'{num} is {state}')



