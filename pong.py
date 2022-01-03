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



# Main game loop

while True:
    window.update()