#sort the by longest name
l = ['Evgeni', 'Georgi', 'Bernard' , 'Martin' , 'Stanislav']
#print(sorted(l, key=len))

#sort by the amount of times we see letter "A" in the names
def count_a(name):
    return name.lower().count('a')

print(sorted(l, key=count_a))




#lamba function = anonymous function