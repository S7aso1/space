# from pathlib import Path 
# p = Path('r-w-txt.txt')
# p.write_text('Writing in file.')
# print(p.read_text())

#---open > r/w > close method

# f = open('r-w-txt.txt', 'r')
# print(f.read())
# f.close()

#---open > r/w > close method
# f = open("r-w-txt.txt", "a") #a = append method
# f.write("Now the file has more content!")
# f.close()

# f = open("r-w-txt.txt", "r")
# print(f.read()) 

#---open > r/w > close method
# f = open("r-w-txt.txt", "w")
# f.write("Woops! I have deleted the content!")
# f.close()
# #open and read the file after the appending:
# f = open("r-w-txt.txt", "r")
# print(f.read()) 