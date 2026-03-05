# Import game modules.
import turtle

# Primary configuration.
wind = turtle.Screen()                    
wind.title("Rackets by blackbird")                                                               
                                                                                                  
wind.bgcolor("black")                                                                              
wind.setup(width=800, height=600)      
wind.tracer(0)                                                                                   

# Racket_1 Configuration.
racket_1 = turtle.Turtle()
racket_1.speed(0)
racket_1.shape("square")
racket_1.shapesize(stretch_wid=5, stretch_len=1)
racket_1.color("blue")
racket_1.penup()
racket_1.goto(-350, 0)

# Racket_2 Configuration.

racket_2 = turtle.Turtle()
racket_2.speed(0)
racket_2.shape("square")
racket_2.shapesize(stretch_wid=5, stretch_len=1)
racket_2.color("yellow")
racket_2.penup()
racket_2.goto(350, 0)

# Ball Configuration.

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

#### score ###
# /\/\/\/\/\ #
# \/\/\/\/\/ #
####Config####

score_1 = 0
score_2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player:1 0 player:2 0", align="center",font=("courier",12,"normal"))
                                                        

### Functions ###
def racket_1_up():
    y = racket_1.ycor()
    y +=40
    racket_1.sety(y)

def racket_1_down():
    y = racket_1.ycor()
    y -=40
    racket_1.sety(y)

def racket_2_up():
    y = racket_2.ycor()
    y +=40
    racket_2.sety(y)

def racket_2_down():
    y = racket_2.ycor()
    y -=40
    racket_2.sety(y)


### Keyboard Bindings ###
wind.listen()
wind.onkeypress(racket_1_up, "w")
wind.onkeypress(racket_1_down, "s")
wind.onkeypress(racket_2_up, "Up")
wind.onkeypress(racket_2_down, "Down")

### Main Game loop ###
while True:
    wind.update()         

### Move the ball ###
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

### Border check ### 
    if ball.ycor() >290:
       ball.sety(290)
       ball.dy *= -1

    if ball.ycor() <-290:
       ball.sety(-290)
       ball.dy *= -1
            
    if ball.xcor() >390:
       ball.goto(0, 0)
       ball.dx *= -1
       score_1 += 1
       score.clear()
       score.write("Player:1 {} player:2 {}".format(score_1, score_2), align="center",font=("courier",12,"normal"))
    
    
    if ball.xcor() <-390:
       ball.goto(0, 0)
       ball.dx *= -1
       score_2 += 1
       score.clear()
       score.write("Player:1 {} player:2 {}".format(score_1, score_2), align="center",font=("courier",12,"normal"))
    
    
    ### Rackets touches ###
    # المضرب الثاني (الأصفر) جهة اليمين
    # Racket( Yellow ) of the Right side.
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < racket_2.ycor() + 50 and ball.ycor() > racket_2.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    # المضرب الأول (الأزرق) جهة اليسار
    # Racket ( Blue ) on the left side.
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < racket_1.ycor() + 50 and ball.ycor() > racket_1.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1