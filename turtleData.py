from turtle import Turtle

tim = Turtle()
tom = Turtle()
timmy = Turtle()
tommy = Turtle()
tomi = Turtle()

tim.penup()
tom.penup()
timmy.penup()
tommy.penup()
tomi.penup()

turtleData = [
    {"turtle": tim, "color": tim.color('red'), "position": tim.setpos(-400, 0), "turtle_color": "red"},
    {"turtle": tom, "color": tom.color('green'), "position": tom.setpos(-400, 50), "turtle_color": "green"},
    {"turtle": timmy, "color": timmy.color('blue'), "position": timmy.setpos(-400, 100), "turtle_color": "blue"},
    {"turtle": tommy, "color": tommy.color('purple'), "position": tommy.setpos(-400, -100), "turtle_color": "purple"},
    {"turtle": tomi, "color": tomi.color('yellow'), "position": tomi.setpos(-400, -50), "turtle_color": "yellow"}
]
