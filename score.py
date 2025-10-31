from turtle import Turtle
file = open("highscore.text")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.text") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0,340)
        # self.write(f"Score : {self.score}",align="center",font=("Arial",24, "normal"))
        self.hideturtle()
        self.penup()
        self.update_score()

    def update_score(self):
        self.clear()  # screen se purana score hatao
        self.write(f"Score: {self.score} High Score : {self.highscore}", align="center", font=("Courier", 24, "normal"))
    
    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset_score(self):
        if self.score>self.highscore:
            self.highscore = self.score
            with open("highscore.text",mode="w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.update_score()

 



      
        
