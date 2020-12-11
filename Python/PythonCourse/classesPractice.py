class Person:
    numOfHands = 2
    numOfLegs = 2
    numOfeyes = 2

    def __init__(self, fn,ln):
        print('the __init__ is called')
        self.first_name = fn
        self.last_name = ln

    def getFullName(self):
        print('getting the full name' )
        return self.first_name + ' ' + self.last_name

    def changeFirstName(self, newFirstName):
        print('changing the first name')
        self.first_name = newFirstName