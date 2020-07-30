#comeback2

name = input('what is your name?')
age = input('what is your age?')
eyes  = input('what are your eyes')
hair  = input('what colour is your hair')
height  = input('what is your height')
weight  = input('what is your weight?')


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
