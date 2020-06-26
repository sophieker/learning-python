from datetime import datetime

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

def main():
    n = int(input('Enter index of fib: '))
    prev = datetime.now()
    print(fib(n))
    after = datetime.now()
    print(after - prev)

if __name__ == "__main__":
    main()
