#! /usr/bin/env python3

# MOUCTAR DIALLO
# November 25, 2014
# A program that display balls bouncing on a Monitor

from graphics import *
from random import*

class Ball:
    "create a ball class"
    def __init__(self,win):
        self.oldx = randrange(26,475)
        self.oldy = randrange(26,285)
        circle = Circle(Point(self.oldx, self.oldy), 5)
        circle.draw(win)
        self.ball = circle
        self.dx = randrange(1,3)
        self.dy = randrange(1,3)
        self.win = win        
    def move(self):
        '''bounce the balles to the wall, first get the hight and lengh
        of the cordinate, '''
        self.ball.move(self.dx, self.dy,)
        if self.ball.getCenter().getX() < 25:
            self.dx *= -1
            self.ball.setFill(color_rgb(randrange(256),randrange(256),
                                        randrange(256)))
        elif self.ball.getCenter().getX() > 475:
            self.dx *= -1
            self.ball.setFill(color_rgb(randrange(256),randrange(256),
                                        randrange(256)))
        if self.ball.getCenter().getY() < 25:
            self.dy *= -1
            self.ball.setFill(color_rgb(randrange(256),randrange(256),
                                        randrange(256)))
        elif self.ball.getCenter().getY() > 285:
            self.dy *= -1
            self.ball.setFill(color_rgb(randrange(256),randrange(256),
                                        randrange(256)))
def oval(win):
    '''draw an oval using point(400,395)(100,490)'''
    oval = Oval(Point(400,395), Point(100,490))
    oval.draw(win)
    oval.setFill('darkGray')
def rectangle(win):
    '''draw a cet of rectangle and return each rectangle'''
    r1 = Rectangle(Point(275,405), Point(220,310))
    r1.draw(win)
    r1.setFill('black')
    r2 = Rectangle(Point(490,10),Point(10,310))
    r2.draw(win)
    r2.setFill('darkGray')
    r3 = Rectangle(Point(480,20), Point(20,290))
    r3.draw(win)
    r3.setFill('white')
def circle(win):
    '''draw a circle using point(470,300)radius 5'''
    circle = Circle(Point(470,300), 5)
    circle.draw(win)
    circle.setFill('green')
def main():
    #create a monitor using the functions
    win = GraphWin('Monitor ', 500, 500)
    oval(win)  
    rectangle(win)
    circle(win)
    #call the class 
    balls = [Ball(win)]
    # add 30 balls to win
    for i in range (30):
        balls.append(Ball(win)) 
    while win.checkMouse() is None:
        for ball in balls:
            ball.move()
    #close the window    
    win.close()
    

main()
