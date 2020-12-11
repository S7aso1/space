l = list(range(100))

def find(sortedList, n):
    r = n in sortedList
    return r 

def sbinary(sortedList, n):
    minIndex = 0
    maxIndex = len(sortedList)-1

    while minIndex < maxIndex:

        middleIndex = (maxIndex - minIndex) // 2
        middleValue = sortedList[middleIndex]
        if n == middleValue:
            return True
        elif n < middleValue:
            maxIndex = middleIndex
        else: 
            minIndex = middleIndex + 1 
    return False

sbinary([3,5,6,7], 3)