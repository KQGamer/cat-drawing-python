import turtle
t = turtle.Turtle()
t.speed(100)
t.pensize(5)

#Cat head
def draw_head():
    t.penup()
    t.goto(70.5, 30)
    t.setheading(45)
    t.pendown()
    t.circle(80,90)
    t.circle(100,90)
    t.circle(80,90)
    t.circle(100,90)
draw_head()

#Teleport function
def teleport(x, y, heading=0):
    t.penup()
    t.goto(x, y)
    t.setheading(heading)
    t.pendown()
teleport(-40, 70)

#Cat left eye
def draw_left_eye():
    t.fillcolor('black')
    t.begin_fill()
    t.circle(27) #Left eye
    t.end_fill()
draw_left_eye() 

#Cat white pupil left 
teleport(-48, 95)
t.fillcolor('white')
t.begin_fill()
t.circle(12) #White pupil left
t.end_fill()

#Cat right eye
teleport(40, 70)
def draw_right_eye():
    t.fillcolor('black')
    t.begin_fill()
    t.circle(27) #Right eye
    t.end_fill()
draw_right_eye() 

#Cat white pupil right
teleport(32, 95)
t.fillcolor('white')
t.begin_fill()
t.circle(12) #White pupil right
t.end_fill()

#Cat right whiskers
teleport(92, 90, 0)

def draw_right_whiskers():
    t.left(20)
    t.forward(30)
    t.backward(30)
    t.right(20)
    teleport(92, 80, 0)
    t.right(20)
    t.forward(30)
    t.backward(30)
draw_right_whiskers()

#Cat left whiskers
teleport(-93, 90, 180)
t.right(20)

def draw_left_whiskers():
    t.forward(30)
    t.backward(30)
    t.left(20)
    teleport(-92, 80, 180)
    t.left(20)
    t.forward(30)
    t.backward(30)
draw_left_whiskers()

#Cat nose
teleport(0, 68)
def draw_nose():
    t.fillcolor('black')
    t.begin_fill()
    t.circle(-6) #Nose circle
    t.end_fill()
    teleport(0, 58)
    #Nose bend
    t.left(270)
    t.forward(5)
    t.circle(10, 180)
    t.penup()
    t.goto(0, 58)
    t.pendown()
    t.right(180)
    t.forward(5)
    t.circle(-10, 180)
draw_nose()

#Teleport to draw left ear
teleport(-30, 170, 140)

#Cat left ear
def draw_left_ear():
    t.fillcolor('black')
    t.begin_fill()
    t.forward(60)
    t.left(30)
    t.circle(10,50)
    t.left(40)
    t.circle(214,20)
    t.end_fill()
draw_left_ear()

#Teleport to draw right ear
teleport(30, 170, 40)

#Cat right ear
def draw_right_ear():
    t.fillcolor('black')
    t.begin_fill()
    t.forward(60)
    t.right(30)
    t.circle(-10,50)
    t.right(40)
    t.circle(-214,20)
    t.end_fill()
draw_right_ear()

#Teleport to draw cat body
teleport(-45, 8, 270)

#Cat standing body
def draw_body():
    t.left(-30)
    t.forward(50)
    t.circle(30, 130)
    t.setheading(0)
    t.forward(84)
    t.left(-5)
    t.circle(30, 130)
    t.forward(50)

draw_body()

#Cat legs
def draw_legs():
    teleport(-15, -30, 270)
    t.forward(50)
    teleport(15, -30, 270)
    t.forward(50)
    teleport(40, -55, 270)
    t.forward(23) #Right foot
    teleport(-40, -55, 270)
    t.forward(23) #Left foot
draw_legs()

#Cat tail
def draw_tail():
    teleport(80, -50, 0)
    t.forward(20)
    t.circle(20, 130)
    t.circle(10, 190)
draw_tail()
t.hideturtle()

#FINISH DRAWING A CAT USING PYTHON TURTLE
turtle.done()