
#comeback
from sys import argv
script, age, height, weight = argv

name = 'staso'
eyes = 'green'
hair = 'blonde'

height_convert = int(height) * 0.39
weight_convert = int(weight) * 2.2

print(f"My name: {name}")
print(f"My age: {age}")
print(f"My eyes are: {eyes}")
print(f"My hair {hair}")
print(f"My height {height} centimetres")
print(f"My height {height_convert} in inches")
print(f"My weight {weight} kilograms")
print(f"My weight {weight_convert} in pounds")

total = int(age) + int(height) + int(weight) + int(weight_convert) + int(height_convert)
print(f"If i add all of the numbers i get total: {total}")

print('\n')
