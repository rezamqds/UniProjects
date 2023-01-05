#Full snake game with turtle 🐢

Main Game
while True: #Running an infinite till the collision occurs and then the game ends
wn.update()

 #Ending the game on collision with any of the walls
 if head.xcor() > 280 or head.xcor() < -300 or head.ycor() > 240 or head.ycor() < -240:
  time.sleep(1) #This reduces the speed of snake
  wn.clear()
  wn.bgcolor('blue')
  scoreBoard.goto(0,0)
  scoreBoard.write("GAME OVER\n Your Score is : {}".format(
score), align="center", font=("Courier", 30, "bold"))

#If snake collects food
if head.distance(food) < 20:
 #increasing score and updating the high_score if required
 score += 10
if score > high_score:
 high_score = score
scoreBoard.clear()
scoreBoard.write("Score : {} High Score : {} ".format(
score, high_score), align="center", font=("Courier", 25, "bold"))

#creating food at random location
x_cord = random.randint(-290, 270)
y_cord = random.randint(-240, 240)
food_color = random.choice(['yellow', 'green', 'tomato'])
food_shape = random.choice([ 'triangle', 'circle','square'])
food.speed(0)
food.shape(food_shape)
food.color(food_color)
food.goto(x_cord, y_cord)

# Adding a new segment to the snake
new_segment = turtle.Turtle()
new_segment.speed(0)
new_segment.shape("square")
new_segment.color("white smoke") # giving a new color to the tail
new_segment.penup()
segments.append(new_segment) #adding the segment to the list


# Moving the snake
for i in range(len(segments)-1, 0, -1):
 x = segments[i-1].xcor()
 y = segments[i-1].ycor()
 segments[i].goto(x, y)
if len(segments) > 0:
 x = head.xcor()
 y = head.ycor()
 segments[0].goto(x, y)
move()

#Checking for collision with the body
 for segment in segments:
  if segment.distance(head) < 20:
   time.sleep(1)
   wn.clear()
   wn.bgcolor('blue')
   scoreBoard.goto(0,0)
   scoreBoard.write("\t\tGAME OVER\n Your Score is : {}".format(
   score), align="center", font=("Courier", 30, "bold"))

 time.sleep(delay)

turtle.Terminator()
