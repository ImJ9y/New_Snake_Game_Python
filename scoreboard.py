from turtle import Turtle, Screen
ALIGMENT = "center"
FONT = ("Arial", 20, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as new_score:
            self.highScore = int(new_score.read())
        self.penup()
        self.hideturtle()
        self.color("White")
        self.goto(0, 280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highScore}", move=False, align = ALIGMENT, font = FONT)
    def scored(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        with open("data.txt", mode='w') as new_score:
            if self.score > self.highScore:
                new_score.write(f"{self.score}")
                self.highScore = self.score
            else:
                new_score.write(f"{self.highScore}")
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", move=False, align=ALIGMENT, font=FONT)