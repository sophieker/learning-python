fib = [1, 1]

def next_number(): 
    return fib[len(fib) - 1] + fib[len(fib) - 2]


for x in range(0, 8):
    fib.append(next_number())
    print(fib)



    
