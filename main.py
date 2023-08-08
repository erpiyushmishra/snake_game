

from snake import Snake
import time
from turtle import Screen
from food import Food
from scoreboard import Scoreboard


screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")




game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
# Q.1 I believe that here move method of object snake indicates that we used to
# write coding related to snake movement but when we realised that we would
# have to use these codes again and again we created a python file and created a
# Snake class and introduce move method. why and how did we do this?
# ans. yes you are right
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score_increase()

    # wall collision detection
    if snake.head.xcor() >280 or snake.head.xcor() <-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        scoreboard.game_over()
        game_is_on=False
    for segment in snake.segments[1:]:
            if snake.head.distance(segment)<10:
                game_is_on=False
                scoreboard.game_over()

















screen.exitonclick()