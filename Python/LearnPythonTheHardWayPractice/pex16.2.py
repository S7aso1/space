#comeback
def vitality(boost):
    print(f"your hp will be increased")

hclass = input('whats your class?')

mana_value = 100
hp_value = 100
boost = hp_value + hp_value * 0.10

print(f"Your starter mana is {mana_value}")
print(f"Your starter HP is {hp_value}")

vitality(boost)
print(f"Your hp after vitality boost is {boost}")
