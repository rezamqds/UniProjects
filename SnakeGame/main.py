# import modules
import turtle as tr
import time
import random as rand
# init score and high score
score = 0
high_score = 0

# make turtle setup
tr.bgcolor('black')
tr.title("@rezamqds | Snake Game")
tr.speed(0)

# score print
sc = tr.Turtle()
sc.speed(0)
sc.color("white")
sc.penup()
sc.hideturtle()
sc.goto(0, 350)
sc.write("Score : %d  High Score : %d" % (score, high_score), align="center", font=("Arial", 24, 'normal'))

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

tr.done()

