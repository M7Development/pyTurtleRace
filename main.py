from random import randint
from turtle import Screen

from turtleData import turtleData
from turtleEntity import TurtleEntity

screen = Screen()
screen.setup(820, 400)

turtle_bank = []
for i in turtleData:
    turtle_ = TurtleEntity(i["turtle"], i["color"], i["position"], i["turtle_color"])
    turtle_bank.append(turtle_)

for x in turtle_bank:
    x.clearing_movements()

for x in turtle_bank:
    x.starting_position()

predicted_color = screen.textinput(title="Prediction", prompt="Which turtle will win?")
print(f"You choosed {predicted_color}")
x_ = ""
while x_ == "":
    for x in turtle_bank:
        if x.move_forward(randint(0, 10)) == "finished":
            x.winning_color(predicted_color)
            x_ = "a"
            break

screen.exitonclick()
