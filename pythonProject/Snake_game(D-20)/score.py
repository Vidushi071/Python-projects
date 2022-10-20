from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 22, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.score = 0
        self.level = 1
        with open ("name.txt", mode="r") as Player:
            self.name = Player.read()
        print(self.name)
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 370)
        self.write(f"Player : { self.name}  Level :{self.level} Score : {self.score} High Score : {self.high_score}  ", align=ALIGNMENT,
                   font=FONT)
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Player : {self.name}  Level :{self.level}  Score : {self.score}  High Score : {self.high_score}  ", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            file = open("data.txt", mode='w')
            file.write(str(self.high_score))
            file.close()

        self.score = 0
        self.level = 0

        self.update_scoreboard()


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def player(self):
        self.write("", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        if self.score % 5 == 0:
            self.level += 1


        self.update_scoreboard()

