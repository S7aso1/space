print("Chickens")
print("hens", 25 + 30 / 6)
print("roosters", 100 - 25 * 3 % 4)
print("Eggs")
print ("Eggs are:", 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)
print ("Is it true that 3 + 2 < 5 - 7?")
print(3 + 2 < 5 - 7)
print("What's 3+2?", 3 + 2)
print("What's 5-7?", 5 - 7)
print("OH!")
print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)

# Comeback
from sys import argv
scriptname, chickens, eggs = argv
prompt = '>>>'

print(f"Hello sir, you have {chickens} chickens and {eggs} eggs!")
