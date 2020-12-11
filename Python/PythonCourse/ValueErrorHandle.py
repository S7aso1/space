def get_int():
    while True:
        num = input('pick your number: ')
        try:
            num = int(num)
        except ValueError
            print('this is not a number')
            continue
    return num

y = get_int()

for x in range(1,10):
    print(x, 'x', y, '=', x * y)

# index = 1
# while(index < 10):
#     res = num * index
#     print(f'{num} X {index} = {res} ')
#     res = 0
#     index +=1
