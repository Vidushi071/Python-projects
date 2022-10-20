import turtle
import pandas
screen = turtle.Screen()
screen.title("US states")


image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# def get_mouse_click_coor(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
#
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
count = 0
ans = screen.textinput(title="Guess the state", prompt="Whats another state?").title()
guessed_state=[]
while len(guessed_state) < 50:

    if ans == "Exit":
        missing_state = [state for state in all_states if state not in guessed_state]
        # for state in all_states:
        #     if state not in guessed_state:
        #         missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break


    if ans in all_states:
        count += 1
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["state"] == ans]
        # x_coor = data[data["state"] == ans].x
        # y_coor = data[data["state"] == ans].y
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item(),align="center", font=("Roboto", 8 ,"normal"))
        guessed_state.append(ans)
    ans = screen.textinput(title=f"{count}/50 states", prompt="Whats another state?").title()





# new_turtle.goto(x_coor, y_coor)
# answer = screen.textinput(title="Guess the state",prompt="Whats another state?")
# answer_state = answer.title()
# if answer_state == data[data["state"] ]:
#     turtle.goto(data[data["state"]].x,data[data["state"]].y)

screen.exitonclick()