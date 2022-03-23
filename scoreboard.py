from turtle import Turtle

FONT = ("Consolas", 16, "normal")

class Scoreboard(Turtle):
    
    # Initial parameters
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.pu()
        self.hideturtle()
        self.setpos(-200, 260)
        self.display_score()

    # Displaying the score on the screen
    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score}", False, align="center", font=FONT)

    # Increasing the score
    def increase_score(self):
        self.score += 1

    # Displaying gameover message
    def gameover(self):
        self.clear()
        self.setpos(0, 0)
        self.write(f"GAME OVER. Your score: {self.score}", False, align="center", font=FONT)
