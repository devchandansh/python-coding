""" 
@author: Chandan Sharma
@GitHub: https://github.com/devchandansh/ 
"""

"""
================================================================
A Robot moves in a Plane starting from the origin point (0,0). 
The robot can move toward UP, DOWN, LEFT, RIGHT. 
The trace of Robot movement is as given following:

Assumed the fixed movements: 
UP 5
DOWN 3
LEFT 3
RIGHT 2

The numbers after directions are steps.  
This program is to compute the distance current position after sequence of movements.
================================================================
"""

import math

class Robot:
    
    def __init__(self):
        """ Constructor Function """
        self.start_point = None
        self.start_point_x = 0
        self.start_point_y = 0
        
        self.steps_up = 5
        self.steps_down = 3
        self.steps_left = 3
        self.steps_right = 2
        
        self.coordinate_points = []
        
        # set the start Point
        self.start_point = (self.start_point_x, self.start_point_y)
        self.coordinate_points.append(self.start_point)
        
    
    
    def getStartPoint(self):
        """ Get the Starting Point of Robot """
        print("Start Point:", self.start_point)
        
        return (self.start_point)
    
    
    def getCoordinates(self):
        return self.coordinate_points
    
    
    def moveUp(self, steps=None):
        """ To Move Up """
        if steps is None:
            steps = self.steps_up
        
        self.start_point_y += steps
        self.coordinate_points.append((self.start_point_x, self.start_point_y))
        print("Move Up:", steps)
    
    def moveDown(self, steps=None):
        """ To Move Dowm """
        if steps is None:
            steps = self.steps_down
        
        self.start_point_y -= steps
        self.coordinate_points.append((self.start_point_x, self.start_point_y))
        print("Move Down:", steps)
        
    
    def moveLeft(self, steps=None):
        """ To Move Left """
        if steps is None:
            steps = self.steps_left
        
        self.start_point_x -= steps 
        self.coordinate_points.append((self.start_point_x, self.start_point_y))
        print("Move Left:", steps)
        
    
    def moveRight(self, steps=None):
        """ To Move Right """
        if steps is None:
            steps = self.steps_right
        
        self.start_point_x += steps
        self.coordinate_points.append((self.start_point_x, self.start_point_y))
        print("Move Right:", steps)
        
    
    def get_position(self):
        """ Get the Current Position """
        return (self.start_point_x, self.start_point_y)
    
    
    def get_distance(self):
        # Starting Point
        start_x = self.start_point[0]
        start_y = self.start_point[1]
        
        # Ending Point
        end_pos = self.coordinate_points[len(self.coordinate_points)-1]
        end_x = end_pos[0]
        end_y = end_pos[1]
        
        # Calculation
        distance = math.sqrt( math.pow((end_x - start_x), 2) + math.pow((end_y - start_y),2) )
        
        print("---------------------------")
        print("Distance Calculation:")
        print("Starting Point: ", self.start_point)
        print("Coordinates Points are: ", self.coordinate_points)
        print("distance:", distance)
        print("---------------------------")
        
        return distance
    
    



# Execute the Program:
objRobot = Robot()
objRobot.moveUp()
objRobot.moveDown()
objRobot.moveLeft()
objRobot.moveRight()
distance = objRobot.get_distance()

print(distance)




"""
===========================================
# Output:
===========================================

Move Up: 5
Move Down: 3
Move Left: 3
Move Right: 2
---------------------------
Distance Calculation:
Starting Point:  (0, 0)
Coordinates Points are:  [(0, 0), (0, 5), (0, 2), (-3, 2), (-1, 2)]
distance: 2.23606797749979
---------------------------
2.23606797749979

"""