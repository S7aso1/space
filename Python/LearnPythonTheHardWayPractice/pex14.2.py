#comeback
from os.path import exists

srcfile = input('copy this file ')
destfile = input('and name it: ')

print(f"Copy {srcfile} to {destfile}")
in_file = open(srcfile)
in_data = in_file.read()

print(f"does the output file exist? {exists(destfile)}")
input()

out_file = open(destfile, 'w')
out_file.write(in_data)
out_file.close()
in_file.close()
