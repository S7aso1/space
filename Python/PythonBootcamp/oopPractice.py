# class User:
#     def __init__(self,first,last,age):
#         self.first = first
#         self.last = last
#         self.age = age
    
#     def full_name(self):
#         return f"{self.first} {self.last}"

#     def initials(self):
#         return f"{self.first[0]} {self.last[0]}"


# user1 = User('Joe', 'Bosh', 54)
# user2 = User('Marta', 'Green', 33)

# print(user1.first, user1.last)

########################################################

class Pet:
    allowed = ['cat', 'dog', 'fish', 'rat']
    def __init__(self,name,species):
        if species not in Pet.allowed:
            raise ValueError(f' You cant have {species} as a pet')
        self.name = name
        self.species = species

cat =Pet('blue', 'cat')