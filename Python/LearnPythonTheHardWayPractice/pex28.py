i = 0
numbers = []
#creates an empty list
while i < 6:
    print(f'at the top i is {i}')
    numbers.append(i)


    i = i + 1
    print('numbers now:', numbers)
    print(f'at the bottom i is {i}')


print('the numbers:')

for num in numbers:
    print(num)

def dril1(n):
    i = 0
    numbers1 = []
    while i < n:
        print "item: %d"
        numbers1.append(i)
        i = i + 1
    print numbers1
