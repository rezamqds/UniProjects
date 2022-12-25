# import modules
import turtle as tr
import time
import random as rand

# init score and high score
score = 0
high_score = 0
print("Hello Welcome to @rezamqds 's snake game \n")
GOD = False

name=input("please enter your name: ")
if name == 'god':
    score = 9999
    high_score = 9999
    GOD = True

# make turtle setup
Size = 850
screen = tr.Screen()
screen.setup(width=Size, height=Size)
screen.bgcolor('black')
if GOD:
    screen.title("@rezamqds | Snake Game | GOD!!")
else:
    screen.title("@rezamqds | Snake Game")

# score print
ScoreW = tr.Turtle()
ScoreW.speed(0)
ScoreW.color("white")
ScoreW.penup()
ScoreW.hideturtle()
ScoreW.goto(0, 350)
ScoreW.write("Score : %d  High Score : %d" % (score, high_score), align="center", font=("Arial", 24, 'normal'))
ScoreW.goto(300, -200)
if GOD:
    ScoreW.write("GOD mode ;)")

# Game Border
border = tr.Turtle()
w = 400
border.speed(8)
border.penup()
border.hideturtle()
border.goto(w, w)
border.color('red')
border.pendown()
border.pensize(20)
border.goto(w, -w)
border.goto(-w, -w)
border.goto(-w, w)
border.goto(w, w)

# snake setup
snake = tr.Turtle()
snake.speed(0)
snake.penup()
snake.shape("square")
snake.color("cyan")

# snake2 +
snake2 = tr.Turtle()
snake2.speed(0)
snake2.penup()
snake2.shape("square")
snake2.color("cyan")
snake2.goto(1000, 2000)

# snake3 +
snake3 = tr.Turtle()
snake3.speed(0)
snake3.penup()
snake3.shape("square")
snake3.color("cyan")
snake3.goto(1000, 2000)



# food setup
food = tr.Turtle()
food.speed(0)
food.shape('circle')
food.color('green')
food.penup()
randFood = rand.randint(-350, 350)
ranF = rand.randint(-350, 350)
food.goto(randFood, ranF)


# def for angle of snake

def up():
    snake.setheading(90)
def down():
    snake.setheading(270)
def left():
    snake.setheading(180)
def right():
    snake.setheading(0)


# Move with arrow keys
screen.listen()
screen.onkey(up, 'Up')
screen.onkey(down, 'Down')
screen.onkey(left, 'Left')
screen.onkey(right, 'Right')

screen.listen()
screen.onkeypress(up, 'w')
screen.onkeypress(down, "s")
screen.onkeypress(left, "a")
screen.onkeypress(right, "d")

speed = 3
ScoreW.goto(0, 350)
segments = []
conSize = 380

while True:
    screen.update()
    snake.forward(speed)

    # Game over cond
    if snake.xcor() > conSize or snake.xcor() < -conSize or snake.ycor() > conSize or snake.ycor() < -conSize:

        snake.goto(0, 0)
        # after Game over
        if not GOD:
            ScoreW.goto(0, 10)
            ScoreW.write("GAME OVER")
            snake.color('red')
            score = 0
            time.sleep(1.5)
        if GOD:
            score+=666
        ScoreW.goto(0, 350)
        ScoreW.clear()
        ScoreW.write("Score : %d  High Score : %d" % (score, high_score), align="center", font=("Arial", 24, 'normal'))
        snake.color('cyan')
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()

    if snake.distance(food) < 20:
        randFood = rand.randint(-350, 350)
        ranF = rand.randint(-350, 350)
        food.goto(randFood, ranF)

        # # Adding segment
        # new_segment = tr.Turtle()
        # new_segment.speed(0)
        # new_segment.shape("square")
        # new_segment.color("orange")
        # new_segment.penup()
        # segments.append(new_segment)

        # Score +
        score += 5
        if GOD:
            score+=12
        if score > high_score:
            high_score = score
        ScoreW.clear()
        ScoreW.write("Score : %d  High Score : %d" % (score, high_score), align="center", font=("Arial", 24, 'normal'))

    # # Checking for head collisions with body segments
    # for index in range(len(segments) - 1, 0, -1):
    #     x = segments[index - 1].xcor()
    #     y = segments[index - 1].ycor()
    #     segments[index].goto(x, y)
    # if len(segments) > 0:
    #     x = snake.xcor()
    #     y = snake.ycor()
    #     segments[0].goto(x, y)
    # # move()
    #
    # for segment in segments:
    #     if segment.distance(snake) < 20:
    #         time.sleep(1)
    #         snake.goto(0, 0)
    #         snake.direction = "stop"
    #         snake.shape("square")
    #         snake.color("cyan")
    #         for segment in segments:
    #             segment.goto(1000, 1000)
    #         segment.clear()

    # screen.mainloop()