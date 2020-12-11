# import random
# randomListOne = []
# randomListTwo = []
# repeatedNumbers = []

# for i in range (0,5):
#     n = random.randint(1,10)
#     randomListOne.append(n)

# for i in range (0,5):
#     n = random.randint(1,10)
#     randomListTwo.append(n)

# print(f'List one is: {randomListOne}')
# print(f'List two is: {randomListTwo}')

# repeatedNumbers = set(randomListOne).intersection(randomListTwo) #returns object
# repeatedNums = list(repeatedNumbers) #converts to list
# print(f'The repeating numbers are: {repeatedNums}')

import random
def generate_rand_list(count, maxNumber):
    l = []
    for i in range(count):
        x = randint(0, maxNumber)
        l.append(x)
    return l

l1 = generate_rand_list(100, 10)

common = set(l1).intersection(set(l2))
for x in common:
    print(x)
