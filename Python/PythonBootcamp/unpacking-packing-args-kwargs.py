# numbers = [1,2,3,4,5]
# print(numbers)
# print(*numbers)
# for num in numbers:
#     print(type(num))

# def add(*numbers):
#     total = 0
#     for number in numbers:
#         total = total + number
#     return (total)

# print(add(3,4,5,6))


# def about(name, age, likes):
#     sentence = f'meet {name}! they are {age} years old and they like {likes}'
#     return sentence

# dictionary = {
#     'name':'mike',
#     'age' : 23, 
#     'likes' : 'food'
# } 

# print(about(**dictionary))


def foo(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print(foo(eve = 'female', adam = 'male'))