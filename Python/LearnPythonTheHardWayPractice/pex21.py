def break_words(stuff):
    '''this function will break up words for us'''
    words = stuff.split(' ')
    return words

def sort_words(words):
    '''sorts the words'''
    return sorted(words)

def print_first_word(words):
    '''prints the first word after popping it off'''
    word = words.pop(0)
    print(word)

def print_last_word(words):
    '''prints the last word after popping it off'''
    words = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    '''takes in full sentence and returns the sorted words'''
    words = break_words(sentance)
    return sort_words(sort_words)

def print_first_and_last(sentance):
    '''prints the first and last words of the sentence'''
    words = break_words(sentance)
    print_first_word(sort_words)
    print_last_word()

def print_first_and_last_sorted(sentence):
    '''sorts the words then prints the first and last'''
    words = sort_sentence(sentance)
    print_first_word(words)
    print_last_word(words)
