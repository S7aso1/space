print('you enter a room with 2 doors \n do you go through door 1 or door 2>')

door = input('Make your choise:')

if door == '1':
    print('you have found a chest ')
    print('what do you do?')
    print('1 - open chest')
    print('2 - don`t open chest')

    chest = input('Make your choise:')

    if chest == '1':
        print('the chest was actually a mimic and it devoured you. gg ')
    elif chest == '2':
        print('you stand next to the chest awkwardly')
    else:
        print('chest explodes in Legendary loot')

elif door == '2':
    print('you have found mustakrakish')
    print('1. Engage in battle')
    print('2. Scream like a girl')

    rat = input('Make your choise:')

    if rat == '1':
        print('You struck down the giant rat with your overwhelming awesomeness')
    elif rat == '2':
        print('You scream like a little girl which angers mustakrakish and it bites your head off')
    else:
        print('You stay still, mustakrakish loses interest and leaves')

else:
    print('you turn back to leave the room...COWARD')
