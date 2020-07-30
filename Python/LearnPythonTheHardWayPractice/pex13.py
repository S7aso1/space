from sys import argv
script, filename = argv

print(f"we're going to erase {filename}")
print(f"if you don`t want that hit ctrl + c")
print(f"if you want that hit enter")

input ("?")

print ("Opening the file")
target = open(filename, 'w')#this puts open into write mode,
#without the 'w' flag you cant write

print("Truncating the file")
target.truncate()

print("Now i am going to ask you for three lines")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("i am going to write these to the file")

#target.write(line1)
#target.write('\n')
#target.write(line2)
#target.write('\n')
#target.write(line3)
#target.write('\n')
target.write('{}\n{}\n{}\n'.format(line1, line2, line3))


print("and finally, we close it")
target.close()
