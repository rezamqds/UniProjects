# import modules
import turtle as tr
import time
import random as rand

# init score and high score
score = 0
high_score = 0
print("Hello Welcome to @rezamqds 's snake game \n")
GOD = False

'''
name=input("please enter your name: ")
if name == 'god' or 'GOD' or 'God':
    score = 9999
    high_score = 9999
    GOD = True
'''

# make turtle setup
Size = 850
screen = tr.Screen()
screen.setup(width=Size, height=Size)
screen.bgcolor('black')
if GOD == True:
    screen.title("@rezamqds | Snake Game | GOD!!")
else:
    screen.title("@rezamqds | Snake Game")

# score print
sc = tr.Turtle()
sc.speed(0)
sc.color("white")
sc.penup()
sc.hideturtle()
sc.goto(0, 350)
sc.write("Score : %d  High Score : %d" % (score, high_score), align="center", font=("Arial", 24, 'normal'))
sc.goto(300, -200)
if GOD == True:
    sc.write("GOD mode ;)")

# Game Border
border=tr.Turtle()
w=400
border.speed(8)
border.penup()
border.hideturtle()
border.goto(w,w)
border.color('red')
border.pendown()
border.pensize(20)
border.goto(w,-w)
border.goto(-w,-w)
border.goto(-w,w)
border.goto(w,w)

# snake setup
snake = tr.Turtle()
snake.speed(0)
snake.penup()
snake.shape("square")
snake.color("cyan")
snake.direction = "Stop"

# food setup
food = tr.Turtle()
food.speed(0)
food.shape('circle')
food.color('green')
food.penup()
x = rand.randint(100, 700)
y = rand.randint(100, 700)
food.goto(x, y)



speed = 1
def up():
    snake.setheading(90)
def down():
    snake.setheading(270)
def left():
    snake.setheading(180)
def right():
    snake.setheading(0)



screen.listen()
screen.onkey(up, 'Up')
screen.onkey(down, 'Down')
screen.onkey(left, 'Left')
screen.onkey(right, 'Right')

# set conditions
cond = False
consize = 380
while not cond:
    screen.update()
    snake.forward(speed)

    screen.listen()
    screen.onkeypress('w')
    screen.onkeypress("s")
    screen.onkeypress("a")
    screen.onkeypress("d")

    if snake.xcor() > consize or snake.xcor() < -consize or snake.ycor() > consize or snake.ycor() < -consize:
        cond = True
        snake.color('red')
        snake.goto(0, 0)

        sc.goto(0, 10)
        sc.write("GAME OVER")

        tr.done()

while snake.distance(food) < 20:
    x = rand.randint(10, 600)
    y = rand.randint(10, 600)
    food.goto(x, y)
