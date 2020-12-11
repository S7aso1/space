def funnyAddition():
    numStr = input("Give me a one-digit-number ")
    numInt = int(numStr)

    if numInt >= 0 and numInt <= 9:
        result = int(numStr) + int(2*numStr) + int(3*numStr) + int(4*numStr)
        print(result)

funnyAddition()