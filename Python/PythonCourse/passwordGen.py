from RandomWordGenerator import RandomWord

def levelOne():
    rw = RandomWord(max_word_size=8,
                    constant_word_size=False)
    return rw.generate()
    print(rw.generate())
levelOne()


def levelTwo():
    rw = RandomWord(max_word_size=10,
                    constant_word_size=True,
                    special_chars=r"@#$%.*",
                    include_special_chars=True)
    return rw.generate()
    print(rw.generate())
levelTwo()


def levelThree():
    rw = RandomWord(max_word_size=10,
                    constant_word_size=True,
                    include_digits=True,
                    special_chars=r"-_!{}@#$%.*",
                    include_special_chars=True)
    return rw.generate()
    print(rw.generate())
levelThree()


def howStrong ():
    value = int(input('There are three levels of passwords. Enter number between 1-3 depending on how strong you want your password to be: '))

    if(value == 1):
        print('password strength = 1')
        print(levelOne())

    elif(value == 2):
        print('password strength = 2')
        print(levelTwo())

    elif(value == 3):
        print('password strength = 3')
        print(levelThree())

    else: 
        print('The number is not in the given range! Try again!')

howStrong()




