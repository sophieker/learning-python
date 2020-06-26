import math
A = [1, 4, 6, 9, 10, 14, 16, 17, 25, 37, 47]
element = int(input("What element would you like to search for? "))

def search(array, element, start, end):

    difference = int(end - start)
    if difference == 1:
        return array[start] == element
    else:
        middle = math.ceil((start+end)/2)
        if array[middle] == element:
            return True
        elif array[middle] > element:
            return search(array, element, start, middle)
        else:
            return search(array, element, middle, end)


def main():
    print(search(A, element, 0, len(A)))

if __name__ == "__main__":
    main()

    
