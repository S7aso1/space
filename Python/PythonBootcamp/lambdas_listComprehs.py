# def square(num): return num*num
# print(square(3))

# square2 = lambda num:  num*num
# print(square2(3))

# add = lambda a,b: a + b
# print(add(3,10))

# # #common lambda usecase
# # map - standard funtion, accepts two arguments - function and iterable (list, string, dictionary, sets , tuples)
# # runs the lambda for each value in the iterable and returns a map object which can be converted into another data structure

# nums = [2,3,4,5,6]

# doubles = map(lambda x: x*2 ,nums)
# print(doubles)
# print(list(doubles))

# #-------------------------------------#
# people = ['Darcy', 'Chris', 'Dana']

# peeps = map(lambda name: name.upper(), people)
# print(list(peeps))

# #-------------------------------------#
# names = [
#     {'product id' : 'x1x', 'product price' : '10'},
#     {'product id' : 'x2x', 'product price' : '20'},
#     {'product id' : 'x3x', 'product price' : '30'}
# ]

# prodID = list(map(lambda x: x['product id'], names))

# print(prodID)
# #-------------------------------------#

# arr = [1,2,3,4,5]

# evens = list(filter(lambda x: x % 2 == 0, arr))
# print(evens)
# #-------------------------------------#

# names = ['austin' , 'penny', 'anthony', 'angel', 'billy']
# a_names = filter(lambda n: n[0] == 'a', names)
# print(list(a_names))

# #-------------------------------------#

# users = [
#     {'username': 'andr3', 'tweets': ['i love to cook', 'i like hiking']},
#     {'username': 's4m', 'tweets': ['i like cats']},
#     {'username': 'bob123', 'tweets': []},
#     {'username': 'g16', 'tweets': []},
#     {'username': '3lucky', 'tweets': ['i like dogs']},
#     {'username': 'fam0us', 'tweets': []}
# ]

##PRINT LIST OF OBJECTS WITH INACTIVE USER NAMES AND THEIR EMPTY TWEETS LIST
# inactive_users = list(filter(lambda u: len(u['tweets']) == 0, users))
# print(inactive_users)

##PRINT LIST OF INACTIVE USER NAMES
# usernames = (list(map(lambda user: user['username'],
#     filter(lambda u: len(u['tweets']) == 0, users))))
# print(usernames)

##PRINT LIST OF OBJECTS WITH INACTIVE USER NAMES AND THEIR EMPTY TWEETS LIST WITH LIST COMPREHENSION
# inactive_users2 = [user for user in users if not user['tweets']]
# print(inactive_users2)

##PRINT LIST OF INACTIVE USER NAMES WITH LIST COMPREHENSION
# usernames2 = [user['username'] for user in users if not user['tweets']]
# print(usernames2)

##SORT OBJECT BY MOST ACTIVE USERS
# most_active = sorted(users, key = lambda user: len(user['tweets']), reverse = True)
# print(most_active)
# #-------------------------------------#

# names = ['Paul', 'James', 'Oliver']

# list(map(lambda name: f'Your instructor is {name}', filter(lambda value: len(value) < 5, names)))
# #-------------------------------------#

songs = [
    {'title' : 'Killing in the name of', 'playcount' : 1},
    {'title' : 'Guerrilla Radio', 'playcount' : 40},
    {'title' : 'Bulls on Parade', 'playcount' : 33}
]

# #SORT THE MOST PLAYED SONGS 
# most_played_list = sorted(songs, key = lambda pcount: pcount['playcount'], reverse = True)
# print(most_played_list)

leastPlayedSong = min(songs, key = lambda song: song['playcount'])
mostPlayedSong  = max(songs, key = lambda song: song['playcount'])

print(leastPlayedSong)  
print(mostPlayedSong)