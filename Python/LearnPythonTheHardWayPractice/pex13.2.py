## ComeBack
filename = input('whats the filename')

task = open(filename)

print (f"Your file is {filename} and it contains:\n ")
print (task.read())

task.close()
