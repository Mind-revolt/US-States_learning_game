import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
correct_answers = 0
us_csv = pandas.read_csv("50_states.csv")
all_states = us_csv.state.to_list()
guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Guess another State").title()
    states_column = us_csv["state"]

    if answer_state == "Exit":
        states_missed = [state for state in all_states if state not in guessed_states]
        states_missed_data = pandas.DataFrame(states_missed)
        states_missed_data.to_csv("States2learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        place = turtle.Turtle()
        place.hideturtle()
        place.penup()
        state_ = us_csv[us_csv.state == answer_state]
        place.goto(int(state_.x), int(state_.y))
        place.write(f"{answer_state}", align="center", font=("Times", 10, "normal"))


            # state_ = us_csv[us_csv.state == state]
            # x_cor = int(state_["x"])
            # y_cor = int(state_["y"])
            # place = turtle.Turtle()
            # place.hideturtle()
            # place.penup()
            # place.goto(x_cor, y_cor)
            # place.write(f"{state}", align="center", font=("Times", 10, "normal"))
            # correct_answers += 1

    if correct_answers == 50:
        turtle.Turtle.write("Congratulations! You Won!", align="center", font=("Times", 30, "normal"))

