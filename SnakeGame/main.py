#import modules
import turtle as tr
import time
import random as rand
#init score and high score
score = 0
high_score = 0
#make turtle setup
tr.bgcolor('cyan')
tr.shape('square')
tr.color('red')
tr.penup()

tr.goto(50,40)
target=tr.Turtle()
tr.goto(-50,40)
target.goto(40,100)
tr.done()