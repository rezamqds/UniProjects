# import modules
import turtle as tr
import time
import random as rand

# init score and high score
score = 0
high_score = 0
print("Hello Welcome to @rezamqds 's snake game \n")
x=int(input("!!! Please enter width(X) !!! : "))
y=int(input("!!! Please enter height(Y) !!! : "))
if x==1337:
    score=9999
    high_score=9999
    x=850
    y=850
    God=True
# make turtle setup
screen = tr.Screen()
screen.setup(width=x, height=y)
screen.bgcolor('black')
screen.title("@rezamqds | Snake Game")


# score print
sc = tr.Turtle()
sc.speed(0)
sc.color("white")
sc.penup()
sc.hideturtle()
sc.goto(0, 350)
sc.write("Score : %d  High Score : %d" % (score, high_score), align="center", font=("Arial", 24, 'normal'))
sc.goto(300,-200)
sc.write("GOD mode ;)")
# snake setup
snake = tr.Turtle()
snake.speed(0)
snake.penup()
snake.shape("square")
snake.color("cyan")

# food setup
food = tr.Turtle()
food.speed(0)
food.shape('circle')
food.color('green')
food.penup()
food.goto(-68, 135)


# fun for moving
def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 2)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 2)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 2)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 2)


# update screen
while True:
    tr.update()

tr.done()

