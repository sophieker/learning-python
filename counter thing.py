while True:
    n = int(input('Enter a value of n: '))
    x = []
    y = 1
    for counter in range(0, n):
        x.append(y)
        y = y+counter
    print(x)
    if n == 0:
        break
    
  
