from turtle import Turtle

starting_position= [(0,0),(-20,0),(-40,0)]
RIGHT = 0
LEFT  = 180
UP = 90
DOWN = 270

class Snake:
    
    
    def __init__(self):
        self.segment = []
        self.create_snake()
        
    def create_snake(self):
        for making_snake in  starting_position:
            self.add_segment(making_snake)   
    def add_segment(self,making_snake):
        new_snake = Turtle(shape="square")
        new_snake.penup()
        new_snake.color("white")
        new_snake.goto(making_snake)
        self.segment.append(new_snake)
    def extend(self):
        self.add_segment(self.segment[-1].position())
    def snake_move(self):
       
        for seg_number in range(len(self.segment)-1,0,-1):
            new_X = self.segment[seg_number-1].xcor()
            new_Y = self.segment[seg_number-1].ycor()
            self.segment[seg_number].goto(new_X,new_Y)
        self.segment[0].forward(20)
    def reset(self):
        for seg in self.segment:
            seg.goto(1000,1000)
        self.segment.clear()    
        self.create_snake()
        # self.segment[0]
           
    def right(self):
        if self.segment[0].heading()!= LEFT:
            self.segment[0].setheading(RIGHT)

    def up(self):
        if self.segment[0].heading() != DOWN:
            self.segment[0].setheading(UP)

    def down(self):
        if self.segment[0].heading() != UP:

            self.segment[0].setheading(DOWN)

    def left(self):
        if self.segment[0].heading() != RIGHT:
            self.segment[0].setheading(LEFT)    









