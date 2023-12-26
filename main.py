# Snake game
import time
import turtle
from turtle import Screen
from snake import Snake
from food import Food
from score_board import Scoreboard

screen = Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor("black") #black screen
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down,"Down")
screen.onkeypress(snake.left,"Left")
screen.onkeypress(snake.right,"Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)  # delay

    snake.move()

    #Detect collision with food

    if snake.head.distance(food) < 15: #if snake head is less than 15 pixels than we can be certain they have collided
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()


    #Detect collision with tail
    for segment in snake.segments[1:]: #this is an example of slicing allowing me to skip over the first head
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()











screen.exitonclick()
