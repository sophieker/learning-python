import turtle
import time

# define arrays and sizes
A = [] 
B = []
C = []
Turtles = []

stick_height = 300

# functions for drawing shapes
def draw_line(x, y, angle, length, width, color, t):
    t.up()
    t.goto(x, y)
    t.seth(angle)
    t.down()
    t.color(color)
    t.pensize(width)
    t.forward(length)
    # hack to handle turtle not drawing last line
    t.up()


def draw_disk(centerx, centery, length, height, turtle_num):
    t = Turtles[turtle_num - 1]
    x1 = centerx - int(length/2)
    y1 = centery + int(height/2)
    draw_line(x1, y1, 0, length, 2, "black", t)
    draw_line(x1 + length, y1, 270, height, 2, "red", t)
    draw_line(x1 + length, y1 - height, 180, length, 2, "blue", t)
    draw_line(x1, y1 - height, 90, height, 2, "green", t)



def draw_all_disks(A, B, C):
# peg base is -93
# height is 20
# width is the number * 20
# y position is the position in the array * 20
    for i in range(len(A)):
        draw_disk(-250, -83 + i * 20, A[i] * 20, 20, A[i])
    for i in range(len(B)):
        draw_disk(0, -83 + i * 20, B[i] * 20, 20, B[i])
    for i in range(len(C)):
        draw_disk(251, -83 + i * 20, C[i] * 20, 20, C[i])
        
    

def draw_pegs():
    turtle.bgcolor('light gray')
    for i in range(-250, 251, 250):
        draw_line(i, -93, 90, stick_height, 5, 'black', turtle.getturtle())

def animate_disk():
    pass

def move_disk(begin, finish):

    if begin == 'A':
        temp = A[-1]
        A.pop(-1)
    elif begin == 'B':
        temp = B[-1]
        B.pop(-1)
    else:
        temp = C[-1]
        C.pop(-1)
        
    if finish == 'A':
        A.append(temp)
    elif finish == 'B':
        B.append(temp)
    else:
        C.append(temp)

    print('A: ', A)
    print('B: ', B)
    print('C: ', C)
    print('\n')
        

# recursive alg
def tower_of_hanoi(n , start, end, middle):

    if n==1:
        move_disk(start, end)
        return
    
    tower_of_hanoi(n-1, start, middle, end)
    move_disk(start, end)
    tower_of_hanoi(n-1, middle, end, start) 



# init
turtle_ = turtle.Turtle()
turtle.setup(1000,1000)
turtle.hideturtle()
turtle.title("Tower of HanUi")
turtle.speed(0)
turtle.tracer(0,0)

n = 10
for i in reversed(range(n)):
    # reliance: A is start
    A.append(i + 1)
    Turtles.append(turtle.Turtle())
print('Initial value: ' , A)

#tower_of_hanoi(n,'A','B','C')
draw_pegs()
draw_all_disks(A, B, C)
turtle.done()
