from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_mov = 3
        self.y_mov = 3
        self.move_speed = 0.01


    def move(self):
        new_x = self.xcor() + self.x_mov
        new_y = self.ycor() + self.y_mov
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_mov *= -1

    def bounce_x(self):
        self.x_mov *= -1
        self.move_speed *= 0.9


    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.01
        self.bounce_x()



