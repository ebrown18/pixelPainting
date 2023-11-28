import turtle
import random
import math
from PIL import Image
# Set up the screen
turtle.setup(width=670, height=505)
turtle.bgpic('sunset2.png')
turtle.speed(10)

# Function to draw a mountain range
turtle.color('white')
MAX_SLOPE = 45
MIN_SLOPE = -45
MIN_HEIGHT = -110
def dist_squared(P1,P2):
    return (P1[0]-P2[0])**2 + (P1[1]-P2[1])**2

def mountain(P1,P2):
    if dist_squared(P1,P2) < 9:
        turtle.goto(P2)
        return
    x1,y1 = P1
    x2,y2 = P2
    x3 = random.uniform(x1,x2)
    y3_max = min((x3-x1)*math.tan(math.radians(MAX_SLOPE)) + y1, (x2-x3)*math.tan(-math.radians(MIN_SLOPE)) + y2)
    y3_min = max((x3-x1)*math.tan(math.radians(MIN_SLOPE)) + y1, (x2-x3)*math.tan(-math.radians(MAX_SLOPE)) + y2)
    y3_min = max(y3_min, MIN_HEIGHT)
    y3 = random.uniform(y3_min,y3_max)
    P3 = (x3, y3)
    mountain(P1,P3)
    mountain(P3,P2)
    return

turtle.up()

turtle.goto(-400,MIN_HEIGHT)
turtle.down()



def add_tree_shape():
    turtle.shapesize(0.3,0.3,0)
    turtle.register_shape("tree2.gif")  # Add the tree image as a shape
    turtle.shape("tree2.gif")     # Set the turtle shape to the tree shape
    
def add_bush_shapes():
    turtle.addshape("bush1.gif")   # Add the first bush image as a shape
    turtle.addshape("bush2.gif")  # Add the second bush image as a shape
    turtle.addshape("bush3.gif")  # Add the third bush image as a shape

    

def draw_trees():
    #for _ in range(5):  # Draw 5 trees
      #  x = random.uniform(-400, 400)
      #  y = random.uniform(-100, 0)
        turtle.pensize(0)
        turtle.up() 
        turtle.goto(-340,-100) 
        turtle.down()
        turtle.shapesize(0.3,0.3,0)
        turtle.stamp()
        turtle.up() 
        turtle.goto(-300,-75) 
        turtle.down()
        turtle.shapesize(0.3,0.3,0)
        turtle.stamp()
        turtle.up() 
        turtle.goto(-240,-50) 
        turtle.down()
        turtle.shapesize(0.3,0.3,0)
        turtle.stamp()
        turtle.up() 
        turtle.goto(-280,-25) 
        turtle.down()
        turtle.shapesize(0.3,0.3,0)
        turtle.stamp()
        turtle.up() 
        turtle.goto(340,-100) 
        turtle.down()
        turtle.shapesize(0.3,0.3,0)
        turtle.stamp()
        turtle.up() 
        turtle.goto(300,-75) 
        turtle.down()
        turtle.shapesize(0.3,0.3,0)
        turtle.stamp()
        turtle.up() 
        turtle.goto(240,-50) 
        turtle.down()
        turtle.shapesize(0.3,0.3,0)
        turtle.stamp()
        turtle.setpos(280,-25)
        turtle.up() 
        turtle.goto(280,-25) 
        turtle.down()
        turtle.shapesize(0.3,0.3,0)
        turtle.stamp()

        
def draw_bushes():
    #for _ in range(5):  # Draw 5 bushes
       # x = random.uniform(-400, 400)
        #y = random.uniform(-100, 0)
        turtle.pensize(0)
        turtle.up() 
        turtle.goto(-400,-200) 
        turtle.down()
        turtle.shape(random.choice([ "bush2.gif", "bush3.gif"]))
        turtle.shapesize(0.3,0.3,0)
        turtle.stamp()
        
        turtle.up() 
        turtle.goto(-350,-175) 
        turtle.down()
        turtle.shape(random.choice(["bush2.gif", "bush3.gif"]))
        turtle.shapesize(0.3,0.3,0)
        turtle.stamp()
        
        turtle.up() 
        turtle.goto(-300,-150) 
        turtle.down()
        turtle.shape(random.choice(["bush2.gif", "bush3.gif"]))
        turtle.shapesize(0.3,0.3,0)
        turtle.stamp()
        
        turtle.up() 
        turtle.goto(-250,-160) 
        turtle.down()
        turtle.shape(random.choice(["bush2.gif", "bush3.gif"]))
        turtle.shapesize(0.3,0.3,0)
        turtle.stamp()
        
        turtle.up() 
        turtle.goto(400,-200) 
        turtle.down()
        turtle.shape(random.choice(["bush2.gif", "bush3.gif"]))
        turtle.shapesize(0.3,0.3,0)
        turtle.stamp()
        
        turtle.up() 
        turtle.goto(350,-175) 
        turtle.down()
        turtle.shape(random.choice(["bush2.gif", "bush3.gif"]))
        turtle.shapesize(0.3,0.3,0)
        turtle.stamp()
        
        turtle.up() 
        turtle.goto(300,-150) 
        turtle.down()
        turtle.shape(random.choice(["bush2.gif", "bush3.gif"]))
        turtle.shapesize(0.3,0.3,0)
        turtle.stamp()
        
        turtle.up() 
        turtle.goto(300,-165) 
        turtle.down()
        turtle.shape(random.choice(["bush2.gif", "bush3.gif"]))
        turtle.shapesize(0.3,0.3,0)
        turtle.stamp()

turtle.up()
turtle.goto(-400,MIN_HEIGHT)
turtle.down()


# Draw the scene
turtle.begin_fill()  # Begin filling color under the mountain
mountain((-400, MIN_HEIGHT), (400, MIN_HEIGHT))
turtle.end_fill() 

# Add tree shape and draw trees
add_tree_shape()
add_bush_shapes()
draw_trees()
draw_bushes()




# Hide turtle and display the window
turtle.hideturtle()
turtle.done()
