#FIRST TRY
#def mana_and_hp(mana_value, hp_value):
#    print(f"Your current mana is {mana_value}")
#    print(f"Your current HP is {hp_value}")
#
#mana_and_hp(100, 100)
#
#
##################################################
#SECOND TRY FOR THE SAME THING, DIFFERENT SYNTAX
#def mana_and_hp(mana_value, hp_value):
#    print(f"Your current mana is {mana_value}")
#    print(f"Your current HP is {hp_value}")
#
#mana_value = 100
#hp_value = 100
#
#mana_and_hp(mana_value, hp_value)
#
##################################################
#THIRD TRY BUT WITH ADDITIONAL STUFF
def mana_and_hp(mana_value, hp_value):
    print(f"Your current mana is {mana_value}")
    print(f"Your current HP is {hp_value}")

mana_value = 100
hp_value = 100
vitality = hp_value + hp_value * 0.10

mana_and_hp(mana_value, hp_value)
print(f"Your hp after vitality boost is {vitality}")
