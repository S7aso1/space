def colorize(text,color):
    colors = ('cyan', 'yellow', 'blue', 'green', 'magenta')
    
    if type(text) is not str:
        raise TypeError(f'{text} must be a string')

    if color not in colors:
        raise ValueError(f'{color} is not a valid color')
    print(f'Printed {text} in {color}')


colorize(3,'magenta')