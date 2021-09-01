import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")

writer_turtle = turtle.Turtle()
writer_turtle.penup()
writer_turtle.hideturtle()
FONT = ("Arial", 8, "normal")


correct_answer_nr = 0
not_guessed_states = data["state"].to_list()
while correct_answer_nr < 50:
    answer_state = screen.textinput(title=f"{correct_answer_nr}/50 States Correct", prompt="What's another state name?").title()
    if answer_state == "Exit":
        states_to_learn = pandas.DataFrame(not_guessed_states)
        states_to_learn.to_csv("states_to_learn.csv")
        break
    if answer_state in not_guessed_states:
        x_pos = float(data[data["state"] == answer_state].x)
        y_pos = float(data[data["state"] == answer_state].y)
        writer_turtle.goto(x_pos, y_pos)
        writer_turtle.write(arg=answer_state, align="center", font=FONT)
        not_guessed_states.remove(answer_state)
        correct_answer_nr += 1















screen.exitonclick()
