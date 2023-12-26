from turtle import Turtle
import random
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) #ten by ten circle
        self.color("blue")
        self.speed("fastest")
        self.refresh()
      

    def refresh(self):
        """Allows for the food(circle) to be moved to another location once collided"""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

