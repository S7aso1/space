people = 30
cars = 80
trucks = 160


if cars > people:
    print('we should take cars')
elif cars < people:
    print('we should not take cars')
else:
    print('we cant decide')

if trucks > cars:
    print('that`s too many trucks')
elif trucks < cars:
    print ('maybe we could take the trucks')
else:
    print ('we still cant decide')

if people > trucks:
    print('alright, lets just take the trucks')
else:
    print('fine lets stay home then')

if trucks > people or cars > people:
    print('the air is garbage')
