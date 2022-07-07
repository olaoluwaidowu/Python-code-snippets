"""
   Author: Olaoluwa Idowu
   Student ID: 0372483
   Assignment No: 7
   Title: Robo_Trumps
   Date: 4-02-2022  
"""




# importing modules
from random import choice
from turtle import *

# setting the screen and turtle
screen = Screen()
screen.bgcolor('white')
penup()
hideturtle()

# opens card.txt file 
file = open('cards.txt', 'r')

#initializing robot as a variable that holds a dictionary
robots = {}

# using for loop to add entry for each robot
for line in file.read().splitlines():
    
    name, battery, intelligence, speed, usefulness, colour, image = line.split(', ')
    robots[name] = [battery, intelligence, speed, usefulness, colour, image]
    screen.register_shape(image)
    
    
file.close()

print("Robots: ",'rainbow,',',space,',',bird,',',round,',',jet,',',shades,', "(or random)")
# using the while loop
while True:
    # variable to collect user's input
    robot = input('Choose a robot')

    # code to choose random robots
    if robot == "random":
        robot = choice(list(robots.keys()))
        print(robot)

    # displaying robots and stat
    if robot in robots:
        print(robots[robot])
        stats = robots[robot]
        style = ('Arial', 14, 'bold')
        
        
        clear()
        goto(0, 100)
        shape(stats[5])
        setheading(90)       
        stamp()
        setheading(-90)
        forward(60)

        # code to output stat text
        color(stats[4])
        write('Name: ' + robot, font=style, align='center')
        forward(25)
        write('Battery: ' + stats[0], font=style, align='center')
        forward(25)
        write('Intelligence: ' + stats[1], font=style, align='center')
        forward(25)
        write('usefulness: ' + stats[3], font=style, align='center')
        forward(25)
        write('speed: ' + stats[2], font=style, align='center')
        forward(25)
        
        
        
        
              

    else:
        print('Robot doesn\'t exist')

    
