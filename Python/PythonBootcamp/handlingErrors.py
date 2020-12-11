# while True:
#     try:
#         num = int(input('please enter a number: '))
#     except ValueError:
#         print('that is not a number')
#     else:
#         print('Good job! You entered a valid number!')
#         break
#     finally:
#         print('.....................................')
# print('_____________________________________')

##################################################################
# def divide(a,b):
#     try:
#         result = a/b
#     except ZeroDivisionError: 
#         print('Can`t divide by zero.')
#     except TypeError as err:
#         print('Please give only numbers to the function')
#         print(err)
#     else: 
#         print(f'result is {result}')
# divide(1,2)
# divide(1,'a')