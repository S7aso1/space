from collections import Counter 

def countLetters():
    str = input("Type a string, please: ")
    strArr = list(str)
    c = Counter(strArr)
    return c

print(countLetters())