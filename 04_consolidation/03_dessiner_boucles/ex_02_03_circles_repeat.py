import turtle as t
import math

def drawCirclesInCircle(nCircles, radius, gap):
    t.clearscreen()
    t.speed(10)
    angleStep = 360 / nCircles


    for i in range(nCircles):
        t.up()
        t.forward(gap)
        t.down()
        t.circle(radius)
        t.up()
        t.backward(gap)
        t.down
        t.right(angleStep)
