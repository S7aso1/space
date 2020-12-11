def display_names(first, second):
    print (f'{first} says hello to {second}')

names = {'first': 'Joe', 'second': 'Sarrah'}

display_names(**names)


def easyFormulla(a, b,c ):
    print(a + b * c)

data = {'a': 1, 'b': 2, 'c': 3}
easyFormulla(**data)