from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 60, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)
        self.update_scoreboard()
    #     self.update_scoreboard()
    #
    def update_scoreboard(self):
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    # def update_r_scoreboard(self):
    #     self.write(self.r_score, align=ALIGNMENT, font=FONT)
    # #
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
    #
    # def increase_score(self):
    #     self.score += 1
    #     if self.score % 5 == 0:
    #         self.level += 1
    #
    #     self.clear()
    #     self.update_scoreboard()
    def score_l(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def score_r(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()
