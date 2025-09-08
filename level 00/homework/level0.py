from turtle import *

#we want to paint a house

#step N1: draw a square
width(8)
color ("blue")

right (180)

forward (250)
left (90) 

forward(250)
left(90)

forward (250)
left (90)

forward(250)
color("grey")
begin_fill()
left (45)

forward (175)
left (90)

forward (175)
end_fill()

color("blue")
#end of square 

#drowing a door

left(45)
forward(250)

left(90)
forward(90)

color("green")
begin_fill()
left(90)
forward(140)     #height of the door

right(90)
forward(70)

right(90)
forward(140)
end_fill()

penup()
goto(-220 , -90)
pendown()

left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)

penup()
goto(-30 , -90)
pendown()

right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)

penup()

exitonclick()

