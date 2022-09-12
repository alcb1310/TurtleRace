from turtle import Turtle, Screen

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

screen = Screen()
screen.setup(width=500, height=400)
screen.title("Turtle Race")
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

turtles = []

y_position = -100
for color in colors:
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(color)
    tim.goto(x=-240, y=y_position)
    y_position += 40
    turtles.append(tim)

screen.exitonclick()
