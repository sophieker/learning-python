import turtle
import time

# define arrays and sizes
A = [] 
B = []
C = []
Turtles = []
A_x = -250
B_x = 0
C_x = 250

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

def draw_disk(centerx, centery, length, height, disk_num):
    t = Turtles[disk_num - 1]
    x1 = centerx - int(length/2)
    y1 = centery + int(height/2)
    draw_line(x1, y1, 0, length, 2, "black", t)
    draw_line(x1 + length, y1, 270, height, 2, "black", t)
    draw_line(x1 + length, y1 - height, 180, length, 2, "black", t)
    draw_line(x1, y1 - height, 90, height, 2, "black", t)
    turtle.update()



def draw_all_disks(A, B, C):
# peg base is -93
# height is 20
# width is the number * 20
# y position is the position in the array * 20
    for i in range(len(A)):
        draw_disk(A_x, -83 + i * 20, A[i] * 20, 20, A[i])
    for i in range(len(B)):
        draw_disk(B_x, -83 + i * 20, B[i] * 20, 20, B[i])
    for i in range(len(C)):
        draw_disk(C_x, -83 + i * 20, C[i] * 20, 20, C[i])
        
    

def draw_pegs():
    turtle.bgcolor('light gray')
    for i in [A_x, B_x, C_x]:
        draw_line(i, -93, 90, stick_height, 5, 'black', turtle.getturtle())
    turtle.update()

def animate_disk(orig_x, orig_y, new_x, new_y, disk_num):
    t = Turtles[disk_num - 1]
    t.clear()
    draw_disk(new_x, new_y, disk_num * 20, 20, disk_num)
"""
    while y < 200:
        y = 
        Turtles[turtle_num].clear()
        draw_disk(-250, y, )
        y = y + 0.01
"""
def move_disk(begin, finish):

    if begin == 'A':
        orig_x = A_x
        orig_y = -83 + (len(A) - 1) * 20
        disk = A[-1]
        A.pop(-1)
    elif begin == 'B':
        orig_x = B_x
        orig_y = -83 + (len(B) - 1) * 20
        disk = B[-1]
        B.pop(-1)
    else:
        orig_x = C_x
        orig_y = -83 + (len(C) - 1) * 20
        disk = C[-1]
        C.pop(-1)
    print(type(A), type(disk))
        
    if finish == 'A':
        A.append(disk)
        new_x = A_x
        new_y = -83 + (len(A) - 1) * 20
    elif finish == 'B':
        B.append(disk)
        new_x = B_x
        new_y = -83 + (len(B) - 1) * 20
    else:
        C.append(disk)
        new_x = C_x
        new_y = -83 + (len(C) - 1) * 20

    animate_disk(orig_x, orig_y, new_x, new_y, disk)

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
turtle.tracer(4,0)

n = 4
for i in reversed(range(n)):
    # reliance: A is start
    A.append(i + 1)
    t = turtle.Turtle()
    t.hideturtle()
    Turtles.append(t)
    
print('Initial value: ' , A)

draw_pegs()
draw_all_disks(A, B, C)
tower_of_hanoi(n,'A','B','C')
turtle.done()
