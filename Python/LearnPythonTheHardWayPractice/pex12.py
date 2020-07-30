from sys import argv

script, filename = argv

txt = open(filename)

print (f"Here is your file {filename}:")
print(txt.read())

filename = input("what is the file name")
txt_again = open(filename)

print(txt_again.read())

txt.close()
txt_again.close ()
