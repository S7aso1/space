def add(a, b):
    print(f"adding {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"subtracting {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"multiplying {a} * {b}")
    return a * b

def divide(a, b):
    print(f"dividing {a} / {b}")
    return a / b

def zeroing(a, b, c):
    print(f"zeroing {a} + {b} * {c}")
    return a + b * c

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)
actual_iq = zeroing(100, 100, 0)

print(f"age {age} height {height} weight {weight} iq {iq}")

#puzzle
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print("that becomes:", what , "can you do it by hand?")
#puzzle2
da = subtract(weight, multiply(age, divide(height, add(100, 100))))
print("that becomes:", da , "can you do it by hand?")
