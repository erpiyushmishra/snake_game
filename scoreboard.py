from turtle import Screen, Turtle
from food import Food
FONT = "Courier"
FONT_SIZE = 12

class Scoreboard(Turtle):



    def __init__(self):
        super().__init__()
        self.scores= 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        #Q2.I can call method which is created in this class which is Scoreboard.j
        #how and why?
        self.scoreboard()

    def scoreboard(self):
        self.write(f"Your score: {self.scores} ", move=False, align="center", font=(FONT, FONT_SIZE, 'normal'))

    def score_increase(self):
        self.scores += 1
        self.clear()
        # Q.3if I will not call method scoreboard right now that self.scores is
        # increased to 1 but it will not show on  the screen
        # and as you know that we can call method and attributes inside the class
# here we have used method inside scoreboard class, without assigning object.
# please elaborate it. How and why?
        self.scoreboard()
    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.write("GAME OVER", move=False, align="center", font=('Courier', 12, 'normal') )

