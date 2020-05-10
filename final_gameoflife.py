import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
import sys
import copy

#0 = dead
#1 = live

array_size = int(input("Enter length of array: "))

# rules
# Any live cell with two or three live neighbors survives.
# Any dead cell with three live neighbors becomes a live cell.
# All other live cells die in the next generation. Similarly, all other dead cells stay dead.

def decide_state(current_gen):
    prev_gen = copy.deepcopy(current_gen)
    for i in range (0,array_size):
       for j in range (0,array_size):
            number_alive = 0
            
            # look at neighbores of node i,j
            for x in range (i-1, i+2):
                for y in range (j-1, j+2):
                    # look at neighbor x,y
                    

                    # skip current node
                    if x == i and y == j:
                        continue
                    
                    # skip boundary
                    if x < 0 or x > array_size-1 or y < 0 or y > array_size-1:
                        continue

                    #print(i, j, x, y, prev_gen[x][y])
                    
                    if prev_gen[x][y] == 1:
                        number_alive = number_alive + 1

            #print(i, j, number_alive)
            
            # setting current block 
            if number_alive == 3:
                current_gen[i][j] = 1
            elif number_alive == 2:
                # leave node in current state
                pass
            else:
                current_gen[i][j] = 0


def init_zeros():
    arr = [[0 for i in range (50)] for j in range (50)]

def main():

    arr = [[0 for i in range (array_size)] for j in range (array_size)]

    user_choice = input("Choose a pattern (options: random, corners, alternate, cross, line): ")
    
    if user_choice == "corners":
        arr[0][0] = 1
        arr[1][0] = 1
        arr[0][1] = 1
        arr[array_size-2][0] = 1
        arr[array_size-1][0] = 1
        arr[array_size-1][1] = 1
        arr[0][array_size-2] = 1
        arr[0][array_size-1] = 1
        arr[1][array_size-1] = 1
        arr[array_size-1][array_size-2] = 1
        arr[array_size-1][array_size-1] = 1
        arr[array_size-2][array_size-1] = 1

    if user_choice == "line":
        for x in range(array_size):
            arr[0][x] = 1
            
    if user_choice == "cross":
        for x in range(array_size):
            arr[x][x] = 1
            arr[x][array_size - x - 1] = 1

    if user_choice == "alternate":
        for x in range(0, array_size, 2):
            for y in range(1, array_size, 2):
                arr[x][y] = 1

        for x in range(1, array_size, 2):
            for y in range(0, array_size, 2):
                arr[x][y] = 1

    if user_choice == "outer":
        for x in range(array_size):
            for y in range(array_size):
                if x == array_size - 1 or x == 0 or y == array_size - 1 or y == 0:
                    arr[x][y] = 1
    
    
    if user_choice == "random":
        arr = np.random.choice(2, (array_size,array_size))
        

    plt.ion()


    plt.matshow(arr, fignum=False);
    plt.show()

    plt.pause(4)

    plt.pause(1)


    for b in range (0, 50):
        print("loop iteration: ", b)
        decide_state(arr)
        plt.matshow(arr, fignum=False);
    
        plt.draw()
        plt.pause(0.2)

if __name__ == "__main__":
    main()

    

#if x == 3:
#    status = live
#elif x == 2:
#    status = status
#else:
   # status = dead
