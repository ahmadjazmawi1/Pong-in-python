import turtle
import os

wn=turtle.Screen()
wn.setup(width=800, height=600)
wn.tracer(0)
wn.bgcolor("black")

# Paddle a (paddle on the left)
paddle_a=turtle.Turtle()
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle b (paddle on the right)
paddle_b=turtle.Turtle()
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Score
score_a=0
score_b=0


# the ball

ball=turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.goto (0,0)
ball.penup()
ball.cx=0.2 #change in x 
ball.cy=0.2 # change in y

pr=turtle.Turtle()
pr.speed(0)
pr.color("white")
pr.penup()
pr.hideturtle()
pr.goto(0,250)
pr.write("Player A: 0   Player B: 0", align="center", font=("arial", 20, "normal"))


# move paddle a up 
def move_paddleA_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y) #update the y coor

def move_paddleA_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

# move paddle b up 
def move_paddleB_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y) #update the y coor

#move paddle b down
def move_paddleB_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)

wn.listen()
wn.onkeypress(move_paddleA_up, "w")
wn.onkeypress(move_paddleA_down, "s")
wn.onkeypress(move_paddleB_up, "Up")
wn.onkeypress(move_paddleB_down, "Down")

# Main game loop (where all the meat and potatoes goes)
while True:
    wn.update()

    #move the ball
    ball.setx(ball.cx + ball.xcor()) 
    ball.sety(ball.cy + ball.ycor())

    #check top border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.cy *=-1
    
    #check bottom border
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.cy *=-1

    # check right border
    if ball.xcor() > 390:
        ball.setx(390)
        ball.goto(0,0)
        ball.cx *=-1
        score_a+=1
        pr.clear()
        pr.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("arial", 20, "normal"))

    #check left border
    if ball.xcor() < -390:
        ball.setx(-390)
        ball.goto(0,0)
        ball.cx *=-1
        score_b+=1
        pr.clear()
        pr.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=("arial", 20, "normal"))

    # ball hits paddle a
    if ball.xcor() > -350 and ball.xcor() < -340 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.cx *=-1

    # ball hits paddle b
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.cx*=-1



    

