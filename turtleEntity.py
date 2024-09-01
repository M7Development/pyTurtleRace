from turtle import Screen

screen = Screen()


class TurtleEntity:
    """Constructor for Turtles"""

    def __init__(self, turtle, color, position, turtle_color):
        self.turtle = turtle
        self.color = color
        self.position = position
        self.winner = 800
        self.turtle_color = turtle_color

    def clearing_movements(self):
        self.turtle.clear()

    def starting_position(self):
        self.turtle.shape("turtle")

    def move_forward(self, run):
        self.turtle.forward(run)
        self.winner = self.winner - run
        if self.winner <= 0:
            return "finished"

    def winning_color(self, predicted_color):
        if self.turtle.pencolor().lower() == predicted_color.lower():
            print("Nice! You Win!")
            print(f"Turtle {self.turtle.pencolor()} win's!")
        else:
            print("You Loose!")
            print(f"Turtle {self.turtle.pencolor()} win's!")