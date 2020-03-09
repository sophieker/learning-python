def fibonacci(n):
    if (n == 1):
        tmp = 0
    elif (n == 2):
        tmp = 1
    else:
        tmp = fibonacci(n-1) + fibonacci(n-2)
    return tmp
print(fibonacci(100))

def two_power(n):
    if (n == 1):
        tmp = 2
    else:
        tmp = two_power(n-1) * 2
    return tmp


