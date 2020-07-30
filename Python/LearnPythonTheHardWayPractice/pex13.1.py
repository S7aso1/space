from sys import argv
script, filename = argv

task = open(filename) #krusteno e za lesno chetene

print (f"Your file is {filename} and it contains:\n ")
print (task.read())

task.close() #prosto kazva da zatvori fajla
