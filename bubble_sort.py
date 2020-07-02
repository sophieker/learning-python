a = [3, 5, 21, 8, 1, 4, 6]

def sort_arr(arr):
    def switch(x, y):
        arr[x], arr[y] = arr[y], arr[x]
        print(arr)

    n = len(arr)
    swapped = True

    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n-x):
            if arr[i - 1] > arr[i]:
                switch(i-1, i)
                swapped = True


sort_arr(a)
