address = {
    'country': 'bulgaria',
    'city': 'plovdiv',
    'street': 'gladson'
}

for key in address.keys():
    print(key)

for value in address.values():
    print(value)

for key,value in address.items():
    print(key,value)

'street' in address
'flat' in address

'bulgaria' in address.values()
'134' in address.values()

address2 = address.copy()
print(address2)
address2.clear()
print(address2)

print(address.get('city'))
print(address.get('flat'))


print({num: num**2 for num in [1,2,3,4]})
