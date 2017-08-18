import turtle

# Basico
turtle.forward(100)
turtle.right(90)
turtle.backward(100)
turtle.left(90)
turtle.forward(100)

turtle.reset()

# Cuadrado
side = 50
for i in range(0, 4):
    turtle.forward(side)
    turtle.right(90)

#turtle.color('red')
#turtle.color((30, 45, 189)) # RGB
turtle.hideturtle()

for i in range(0, 4):
    turtle.begin_fill()
    turtle.circle(3) # Circulos
    turtle.end_fill()
    
    turtle.up()
    turtle.forward(side)
    turtle.right(90)
    turtle.down()
turtle.reset()

# Linea inclinada
turtle.setpos(0, 0)
turtle.setpos(100, 100)
turtle.reset()

# Espiral
side = 1
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0) # velocidad
pen.color("#FF0000")

for i in range (1, 360):
  pen.forward(side)
  pen.left(1)
  side = side

pen.reset()
pen.speed(0) # velocidad
  
for i in range (1, 50):
  pen.forward(side)
  pen.left(90)
  side = side + 7
