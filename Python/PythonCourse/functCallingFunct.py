def formulla(n):
    result = 1 
    for i in range(2, n+1):
        result = mul(result,i)
    return result

def mul(a,b):
    return a * b

print(formulla(5))