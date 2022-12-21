#import modules
import turtle as tr
import time
import random as rand
#init score and high score
score = 0
high_score = 0
#make turtle setup
tr.bgcolor('black')
#snake setup
snake = tr.Turtle()
snake.penup()
snake.shape("square")
snake.color("cyan")

tr.done()