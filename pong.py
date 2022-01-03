import turtle

window = turtle.Screen()
window.title("Pong For Pongers")
window.bgcolor("black")
window.setup(width=800, height=600) #This sets up size of the window
window.tracer(0) #stops the window from updating which speeds the game up

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #speed of animation 
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) #speed of animation 
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#Ball
ball= turtle.Turtle()
ball.speed(0) #speed of animation 
ball.shape("square")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = .2
ball.dy = -.2

#function 
def paddle_a_up():
    y = paddle_a.ycor() #defines y cordinates 
    y += 20 # adds 20 pixels to y 
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor() 
    y -= 20 # subtract 20 pixels to y 
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor() #defines y cordinates 
    y += 20 # adds 20 pixels to y 
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor() 
    y -= 20 # subtract 20 pixels to y 
    paddle_b.sety(y)

#keyboard binding
window.listen() # This tells it to listen to keyboard input from turtle module
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")

# Main game loop

while True:
    window.update()

    #ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 #reverses the direction of the ball

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    #left and right border
    if ball.xcor()> 390:
        ball.goto(0)
        ball.dx *= -1

