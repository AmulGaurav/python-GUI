from turtle import Turtle

ALIGNMENT = "left"
FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            with open(file="snake-game/high_score.txt") as file:
                pass
        except:
            with open(file="snake-game/high_score.txt", mode="w") as file:
                file.write("0")
        finally:
            with open(file="snake-game/high_score.txt") as file:
                self.high_score = int(file.read())
        self.hideturtle()
        self.color("white")
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(x=-290, y=245)
        self.clear()
        self.write(
            f"Score: {self.score}\nHigh Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        if self.score > self.high_score:
            with open(file="snake-game/high_score.txt", mode="w") as file:
                file.write(str(self.score))
        self.score = 0
        self.goto(x=0, y=0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
