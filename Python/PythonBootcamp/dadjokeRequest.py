import requests
from random import choice



userInp = input('What joke do you want to see?  ')
url = "https://icanhazdadjoke.com/search"
res = requests.get(
    url, 
    headers={'Accept' : 'application/json'},
    params = {'term' : userInp}
    ).json()

num_joikes = res['total_jokes']
results = res['results']

if num_joikes > 1:
    print(f'There are {num_joikes} jokes. Here is one:')
    print(choice(results)['joke'])
elif num_joikes == 1:
    print('There is one joke.')
    print(results[0]['joke'])
else:
    print(f'sorry could not find a joke about {userInp}')
