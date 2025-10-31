""" My first Game that I make """
from turtle import Screen
import time,snake_class,food
from score import Score
"""Screen Set up """
screen = Screen()
screen.setup(width= 800,height=800)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake= snake_class.Snake()

""" Function of the Snake Game """

screen.listen()
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")


snake_food = food.Food()
score_board= Score()


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.snake_move()
    if snake.segment[0].distance(snake_food) < 15:
        snake_food.refresh()
        snake.extend()
        score_board.increase_score()
  
    if snake.segment[0].xcor() >380 or snake.segment[0].xcor() < -380 or snake.segment[0].ycor()>380 or snake.segment[0].ycor()< -380:
        # game_is_on = False
        score_board.reset_score()
        snake.reset()
    for segment in snake.segment[1:]:
        
        if snake.segment[0].distance(segment)<10:
            # game_is_on = False
            score_board.reset_score()
            snake.reset()

screen.exitonclick()

