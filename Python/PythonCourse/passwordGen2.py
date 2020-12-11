import random
import string


s = input('Strong or weak password (s/w)? ')

if s.strip().lower() == 's':
    length = 12
    chars = string.ascii_letters + string.digits + string.punctuation
else: 
    length = 6
    chars = string.ascii_lowercase

l = []
for i in range(length):
    l.append(random.choice(chars))
print(''.join(l))