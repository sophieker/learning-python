import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

#0 = dead
#1 = live


# rules
# Any live cell with two or three live neighbors survives.
# Any dead cell with three live neighbors becomes a live cell.
# All other live cells die in the next generation. Similarly, all other dead cells stay dead.

def decide_state(np_array):
    np_array_temp = np_array.copy()
    for i in range (0,50):
       for j in range (0,50):
            number_alive = 0
            
            # look at neighbores of node i,j
            for x in range (i-1, i+2):
                for y in range (j-1, j+2):
                    # look at neighbor x,y

                    # skip current node
                    if x == i and y == j:
                        continue
                    
                    # skip boundary
                    if x < 0 or x > 49 or y < 0 or y > 49:
                        continue
                    
                    if np_array_temp[x][y] == 1:
                        number_alive = number_alive + 1
                            
            # setting current block 
            if number_alive == 3:
                np_array[i][j] = 1
            elif number_alive != 2:
                np_array[i][j] = 0
            # else:
            # leave node in current state

            
                


def main():

    np_random = np.random.choice(2, (50,50))
    print(np_random)

    plt.ion()

    plt.matshow(np_random, fignum=False);
    plt.show()

    plt.pause(1)

    for b in range (0, 50):
        print("loop iteration: ", b)
        decide_state(np_random)
        plt.matshow(np_random, fignum=False);
    
        plt.draw()
        plt.pause(1)

if __name__ == "__main__":
    main()

    

#if x == 3:
#    status = live
#elif x == 2:
#    status = status
#else:
   # status = dead
