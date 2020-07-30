# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"argument one: {arg1}, argument two: {arg2}")

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"argument one: {arg1}, argument two: {arg2}")

#this takes one argument
def print_one(arg1):
    print(f"argument one is {arg1}")

#this one takes no arguments
def print_none():
    print(f"no arguments")


print_two("Axe", "Sniper")   
print_two_again("Axe", "Sniper")
print_one("Axe")
print_none()
