import turtle
import random


# color('blue','yellow')

pen = turtle.Turtle()
pen.penup()
pen.goto(0,0)
pen.down()
pen.dot()
while True:
        v1x = 0 
        v1y = 0
        v2x = 250
        v2y = 0
        v3x = 500
        v3y = 100
        point_x = (random.randint(0,100))*-1
        point_y = (random.randint(0,100))*-1
        pen.goto(point_x, point_y)
        pen.down()
        pen.dot()
        pen.penup() 
done()
'''vertex = random.randint(1,3)
x = random.randint(0,500)
y = random.randint(0,100)
if x >= v2x and x <= v3x and y >=v2y and y <= v3y:
   pen.goto(x,y)
   pen.down()
   pen.dot()
   pen.up()

while True:
    vertex = random.randint(1,3)
    x = random.randint(0,500)
    y = random.randint(0,100)
    if vertex == 1:
        midx = (x + v1x)/2
        midy = (y + v1y)/2
    if vertex == 2:
        midx = (x + v2x)/2
        midy = (y + v2y)/2
    if vertex == 3:
        midx = (x + v3x)/2
        midy = (y + v3y)/2
    if x >= v1x and x <= v3x and y >=v1y and y <= v3y:
        pen.goto(midx, midy)
        pen.down()
        pen.dot()
        pen.up()
done()

pen.penup()
pen.hideturtle()

color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()'''
