# numbers = list(range(5))
# # if 0 in numbers:
# #     print('0 is in numbers')

# # for number in numbers: 
# #     print(number)
# i = 0
# while i < len(numbers):
#     print(numbers[i])
#     i+=1
#---------------------------------
# arr = ['black', 'blue', 'gray']
# i = 0

# while i < len(arr):
#     print(f'index {i} is {arr[i]} color')
#     i+=1
#---------List of methods---------
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
#---------------------------------

# arr = ['a',2,2,2,3,4,'z']
# arr.append('x')
# arr.extend(['extend', 'the', 'the', 'list'])
# arr.insert(1, 'b')
# letterA = arr.pop(0)
# arr.remove('the')

# print(arr)
# print(arr, letterA)
# print(arr.count(2))

# nums = ['extend', 'the', 'the', 'list']
# slicer = nums[1:3]
# Secslicer = nums[:3]
# nums.reverse()
# strng = ' '.join(nums)

# print(nums)
# print(strng)
# print(slicer)
# print(Secslicer)
#----------Reverse a string----------
stringg = 'This is a test'
newString = stringg[::-1]
print(newString)