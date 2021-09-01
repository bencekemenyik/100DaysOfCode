from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
RIGHT = 0
DOWN = 270




class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head_of_the_snake = self.segments[0]
        self.tail_of_the_snake = self.segments[-1]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())


    def reset(self):
        for segment in self.segments:
            segment.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head_of_the_snake = self.segments[0]
        self.tail_of_the_snake = self.segments[-1]


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x=new_x, y=new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if int(self.head_of_the_snake.heading()) != DOWN:
            self.head_of_the_snake.setheading(UP)

    def left(self):
        if int(self.head_of_the_snake.heading()) != RIGHT:
            self.head_of_the_snake.setheading(LEFT)

    def down(self):
        if int(self.head_of_the_snake.heading()) != UP:
            self.head_of_the_snake.setheading(DOWN)

    def right(self):
        if int(self.head_of_the_snake.heading()) != LEFT:
            self.head_of_the_snake.setheading(RIGHT)
