#make the pex14.py work but shorter code
from sys import argv
from os.path import exists

script, from_file, to_file = argv

#make these two on one line
in_file = open(from_file)
indata = in_file.read()
#indata = open(from_file).read()

print(f"does the output file exist? {exists(to_file)}")
input()

out_file = open(to_file, 'w')
out_file.write(indata)
