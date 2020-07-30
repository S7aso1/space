name = 'staso'
age = 21
eyes = 'green'
hair = 'blonde'
height = 180.0
weight = 67.0
height_convert = height * 0.39
weight_convert = weight * 2.2


print(f"My name: {name}")
print(f"My age: {age}")
print(f"My eyes are: {eyes}")
print(f"My hair {hair}")
print(f"My height {height} centimetres")
print(f"My height {height_convert} in inches")
print(f"My weight {weight} kilograms")
print(f"My weight {weight_convert} in pounds")


total = age + height + weight + weight_convert + height_convert
print(f"If i add all of the numbers i get total: {total}")
