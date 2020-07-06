a = [3, 5, 21, 8, 1, 3]

def sort_arr(arr):
    def switch(x, y):
        arr[x], arr[y] = arr[y], arr[x]

    n = len(arr)
    switched = True

    x = -1
    while switched:
        switched = False
        x = x + 1
        print(arr)
        for i in range(1, n-x):
            if arr[i - 1] > arr[i]:
                switch(i-1, i)
                switched = True

sort_arr(a)
