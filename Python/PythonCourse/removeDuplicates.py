finalArr = []

def takeList():
    inputDigits = input('Give me 4 digits: ')
    if (len(inputDigits) > 4):
        print('You gave me more than 4 digits')
    else: 
        inputArr = list(inputDigits)
        finalArr = [int(i) for i in inputArr]
        print(f'Your input array looks like : {finalArr}')
        finalArr = list(dict.fromkeys(finalArr))
        print(f'After removing your duplicate values, the array looks like : {finalArr}')
takeList()