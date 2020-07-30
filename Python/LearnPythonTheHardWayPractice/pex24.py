people = 100
cats = 45
dogs = 50


if people < cats:
    print ("too many cats! the world is doomed!")

if people > cats:
    print ("not many cats! the world is saved!")

if people < dogs:
    print ("the world is drooled on!")

if people > dogs:
    print ("the world is dry!")


dogs +=  5

if people >= dogs:
    print("people are greater than or equal to dogs")

if people <= dogs:
    print("people are less than or equal to dogs")

if people == dogs:
    print("people are dogs")

if cats == dogs or people >= dogs:
    print("Cats are equal to dogs or people are greater than dogs")
