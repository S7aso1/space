from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copy {from_file} to {to_file}")

#make these two on one line
in_file = open(from_file)
indata = in_file.read()

print(f"the input file is {len(indata)}  bytes long")

print(f"does the output file exist? {exists(to_file)}")
print("ready, hit enter to continue, hit crl + c to abort")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("done")

out_file.close()
in_file.close()
