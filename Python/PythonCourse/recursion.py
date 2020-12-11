#recursion
def f(n):
    if n <= 1:
        return 1
    return f(n-1) + f(n-2)

l = []
for i in range(20):
    l.append(f(i))
print(l)

# list comprehention
#l =[f(i) for i in range[20]]