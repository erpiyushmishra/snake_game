from turtle import Turtle
STARTING_POSITIONS=[(0,0), (-20,0), (-40,0)]

MOVE_DISTANCE = 20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:


    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
# what we want from this code: add a square containing all attributes of self
#object to the main body of snake, when a new position is added in
# STARTING_POSITIONS
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
#what we want from this code: when food will be eaten by snake one new
#location will be added in STARTING.POSITION
#will be used by extend as well as create snake
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
#here we are adding one square block of 20*20 to the previous snake, as this will
#repeat itself again and again we must create a new method
#this is totally different code as this is being used in main.py,
# can we say that either method will be used
        # to extend the length of snake by adding new segment
# here add_segment is method to add a new position in our list segments and also
# add_segment is adding a square block at last position in list of blocks
#(i.e sanke)
        self.add_segment(self.segments[-1].position())


    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num-1].xcor() # how, segments know xcor()
            new_y = self.segments[seg_num-1].ycor()

            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
#note:heading():Return the turtle’s current heading (value depends on

        if self.head.heading()!=DOWN:
            self.segments[0].setheading(UP)
    def down(self):
        if self.head.heading()!=UP:
            self.segments[0].setheading(DOWN)
    def left(self):
        if self.head.heading()!=RIGHT:
            self.segments[0].setheading(LEFT)
    def right(self):
        if self.head.heading()!=LEFT:
            self.segments[0].setheading(RIGHT)

