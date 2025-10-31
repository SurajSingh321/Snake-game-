from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self ):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        
        self.speed("fastest")
        self.refresh()
    def refresh(self):
        x = random.randint(-400,400)
        y = random.randint(-400,400)
        self.goto(x,y)



  
