the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this frist kind of for-loop goes through a list
for number in the_count:
    print(f'this is count {number}')

#same as above
for fruit in fruits:
    print(f'a fruit of type {fruit}')

#we can go through mixed lists too
#notice we have to use {} since we dont know whats in it
for i in change:

    print(f'I got {i}')

#we can also build lists, first start with empty one
elements = []

#then use range funcion to do 0 to 5 counts
for i in range (0, 6):
    print(f'adding {i} to the list')
    #append is a function that lists understand
    elements.append(i)

#now we can print them out too
for i in elements:
    print(f'element was: {i}')

# for ok in range (3, 30, 9):
#     print(f'numbers from 3 to 30 with step 9: {ok}')

# for ok in range(4):
#     print(f'print the first 4 numbers using range \n{ok}')
#     print(ok, end ='')
