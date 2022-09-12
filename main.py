from turtle import Turtle, Screen
from random import randint

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

screen = Screen()
screen.setup(width=500, height=400)
screen.title("Turtle Race")
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

turtles = []

y_position = -100
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(x=-240, y=y_position)
    new_turtle.speed("slow")
    y_position += 40
    turtles.append(new_turtle)


winner = -1
is_race_on = True

while is_race_on:
    for index in range(0, 6):
        speed = randint(1, 10)
        turtles[index].fd(speed)

        pos = turtles[index].position()
        if pos[0] >= 230:
            winner = index
            is_race_on = False


if user_bet == colors[winner]:
    print("You win!!")
else:
    print("You loose!")

print(f"The winner is {colors[winner]}")


screen.exitonclick()
